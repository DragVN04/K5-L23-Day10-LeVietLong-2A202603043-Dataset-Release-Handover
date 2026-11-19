#!/usr/bin/env python3
"""Rule Validator — Detection & File (Phần của Bạn A).

Kiểm tra các loại lỗi luật phía File & Detection chỉ dùng thư viện chuẩn của Python:
1. missing_image : manifest có ảnh nhưng thiếu file trên đĩa.
2. wrong_hash    : sha256 thực tế của file khác với sha256 ghi trong manifest.json.
3. invalid_class : class_id trong nhãn YOLO nằm ngoài tập lớp hợp lệ (0..79).
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


def sha256_file(path: Path) -> str:
    """Tính mã băm SHA-256 (hex thường) trên bytes thực tế của file."""
    return hashlib.sha256(path.read_bytes()).hexdigest().lower()


def load_manifest_items(delivery_dir: Path) -> tuple[dict[str, dict], int]:
    """Đọc danh sách items và num_classes từ manifest.json."""
    manifest_path = delivery_dir / "manifest.json"
    if not manifest_path.is_file():
        raise FileNotFoundError(f"Không tìm thấy {manifest_path}")
    doc = json.loads(manifest_path.read_text(encoding="utf-8"))
    items = doc.get("items", {})
    num_classes = int(doc.get("num_classes", 80))
    return items, num_classes


def load_valid_classes(delivery_dir: Path, default_num_classes: int = 80) -> set[int]:
    """Đọc tập class_id hợp lệ từ classes.txt (mặc định 0..default_num_classes-1)."""
    classes_path = delivery_dir / "classes.txt"
    if classes_path.is_file():
        valid: set[int] = set()
        for line in classes_path.read_text(encoding="utf-8").splitlines():
            parts = line.strip().split()
            if parts:
                try:
                    valid.add(int(parts[0]))
                except ValueError:
                    continue
        if valid:
            return valid
    return set(range(default_num_classes))


def parse_yolo_file(label_path: Path) -> list[list[str]]:
    """Đọc các dòng khác rỗng của file nhãn YOLO."""
    if not label_path.is_file():
        return []
    rows: list[list[str]] = []
    for line in label_path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped:
            rows.append(stripped.split())
    return rows


def check_missing_image(delivery_dir: Path, manifest_items: dict[str, dict]) -> list[dict]:
    """1. missing_image: manifest có ảnh nhưng thiếu file trên đĩa."""
    errors: list[dict] = []
    for name, info in manifest_items.items():
        img_rel = info.get("image", f"images/{name}.jpg")
        img_path = delivery_dir / img_rel
        if not img_path.is_file():
            errors.append({"type": "missing_image", "target": name})
    return errors


def check_wrong_hash(
    delivery_dir: Path,
    manifest_items: dict[str, dict],
    missing_images: set[str] | None = None,
) -> list[dict]:
    """2. wrong_hash: sha256 thực tế của file khác với sha256 ghi trong manifest.json."""
    skip = missing_images or set()
    errors: list[dict] = []
    for name, info in manifest_items.items():
        if name in skip:
            continue
        img_rel = info.get("image", f"images/{name}.jpg")
        img_path = delivery_dir / img_rel
        if not img_path.is_file():
            continue
        expected_hash = str(info.get("image_sha256", "")).strip().lower()
        actual_hash = sha256_file(img_path)
        if not expected_hash or actual_hash != expected_hash:
            errors.append({"type": "wrong_hash", "target": name})
    return errors


def check_invalid_class(
    delivery_dir: Path,
    manifest_items: dict[str, dict],
    valid_classes: set[int],
) -> list[dict]:
    """3. invalid_class: class_id không phải số nguyên trong tập lớp hợp lệ (0..79)."""
    errors: list[dict] = []
    for name, info in manifest_items.items():
        label_rel = info.get("label", f"labels/{name}.txt")
        rows = parse_yolo_file(delivery_dir / label_rel)
        has_invalid = False
        for row in rows:
            if not row:
                continue
            try:
                cls_id = int(row[0])
            except ValueError:
                has_invalid = True
                break
            if cls_id not in valid_classes:
                has_invalid = True
                break
        if has_invalid:
            errors.append({"type": "invalid_class", "target": name})
    return errors

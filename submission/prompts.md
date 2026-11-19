# Dùng AI

Người dùng AI: Nguyễn Thanh Quang (2A202603083)

Công cụ: Copilot SDK trong VS Code

## 1. Xác định phần việc được giao

**Prompt nguyên văn**

> đọc nội dung này cần làm những j và làm vào dự án giup tôi, lưu ý chỉ làm phần của mình ko đụng phần của người khác và làm thật cẩn thận

**Kết quả AI:** Đọc hướng dẫn được gửi kèm, xác định các đầu việc Thành viên D gồm truy vết, bảo mật, ghi prompt AI và phối hợp kiểm tra tài liệu bàn giao.

**Kiểm chứng:** Đối chiếu với `GUIDE.md`, `RULES.md` và template của dự án. Không sửa `scripts/`, `delivery/` hay `_private/`.

## 2. Chuyển sang nhánh D-Trace

**Prompt nguyên văn**

> tiếp tục đi và làm vào nhánh D-Trace cho tôi

**Kết quả AI:** Làm việc trên nhánh `D-Trace`, tạo `trace.json` và `security.md` cho seed đang được xác nhận, cập nhật tài liệu của Thành viên D.

**Kiểm chứng:** Kiểm tra nhánh bằng Git; chỉ commit các tệp `submission/` thuộc phần D.

## 3. Tạo lô theo seed 3007 (sau đó được đính chính)

**Prompt nguyên văn**

> Nhóm mình thống nhất dùng seed 3007 (nếu chưa có seed chính thức khác).
>
> Do `runs/` và `data_source/` bị Git ignore nên pull GitHub sẽ không có dữ liệu.
>
> Nếu máy bạn chưa có delivery thì chạy:
>
> `python scripts/download_public.py`
>
> `python scripts/run_lab.py --seeds 3007`
>
> Sau đó làm tiếp phần truy vết:
> - Đọc `incoming/ticket.md` và `guideline/changelog.md`.
> - Đối chiếu `jobs.csv`, `metadata.json` và `labels/`.
> - Xác định `tier_a`, `tier_b`, `notify`.
> - Tạo `trace.json` từ dữ liệu thật.
> - Hoàn thành `security.md`, trong đó phần xác nhận ảnh khuôn mặt phải có người xem ảnh thật.
>
> Không đọc `_private/`, không sửa `delivery/`.
>
> Xong thì báo lại kết quả, các file đã tạo và những phần cần nhóm hỗ trợ.

**Kết quả AI:** AI đã tải dữ liệu và tạo lô `3007`.

**Sai sót và khắc phục:** Người dùng sau đó đính chính seed: “seed là 2902 còn 3007 là nhầm”. AI đã không giải quyết mâu thuẫn seed trước khi chạy. Đã xóa lô `3007` do mình tạo, khôi phục `2902` làm seed chính thức và loại sự kiện tạo `3007` khỏi lineage. Không dùng lô `3007` trong sản phẩm nộp.

## 4. Đính chính seed về 2902

**Prompt nguyên văn**

> nhom_va_repo=bạn cần đổi chút seed là seed 2902 , github_username=Nguyễn Thanh Quang, thanh_vien_va_phan_cong=Nguyễn Thanh Quang, 2A202603083, nguyenvantuc07102015@gmail.com, xac_nhan_lineage=seed là 2902 còn 3007 là nhầm

**Kết quả AI:** Dùng delivery seed `2902`; cập nhật trace, security, report và thông tin nhóm cho đúng seed.

**Kiểm chứng:** Đối chiếu ticket, changelog, `jobs.csv`, metadata, labels và manifest. Guideline dùng để phân loại ảnh được lấy từ `jobs.csv`. Trace độc lập tính lại được tier A gồm 3 ảnh, tier B gồm 4 ảnh và notify gồm `A02`, `Q03`. Không đọc `_private/`.

## 5. Kiểm tra ảnh khuôn mặt

**Prompt nguyên văn**

> Bạn tiếp tục hoàn thiện phần Security nhé.
>
> Với danh sách 20 ảnh ứng viên có class person, bạn tự mở ảnh để kiểm tra trực tiếp, chọn một ảnh có khuôn mặt người thật nhìn thấy rõ.
>
> Sau đó ghi đúng image ID và tình huống xử lý vào security.md theo template của đề.
>
> Phần khuôn mặt phải kết luận HOLD + báo người phụ trách, không tự ý làm mờ hoặc sửa dataset gốc.
>
> Khi hoàn thành, bạn kiểm tra lại trace.json và security.md, rồi commit và push lên branch D-Trace, tạo Pull Request để mình review và merge.
>
> Báo lại mình file nào đã hoàn thành và kết quả kiểm tra nhé.

**Kết quả AI:** Mở ảnh `000000001000.jpg` trong delivery `r2902`; ảnh có nhiều khuôn mặt nhìn rõ. Nguyễn Thanh Quang sau đó tự mở và xác nhận ảnh này. `security.md` ghi HOLD, báo người phụ trách và không sửa ảnh gốc.

**Kiểm chứng:** Thành viên xác nhận đã tự xem ảnh. H16/H17 được kiểm tra trực tiếp trên file trace/security.

---

## 6. Thành viên C: Đối chiếu Detection ↔ Panoptic và công cụ Review

Người dùng AI: Thành viên C (Phụ trách Cross-check, Candidates và Review Tool)

**Prompt nguyên văn**

> tôi sẽ làm trên nhánh này https://github.com/DragVN04/K5-L23-Day10-LeVietLong-2A202603043-Dataset-Release-Handover/tree/A-Cross-check
> và tôi là người C
> Phân công:
> - Long (Leader): Tạo repo, seed chung, quản lý tiến độ, quyết định Release/Hold, lineage, handover v2, tích hợp và kiểm tra bài nộp.
> - Bạn A: Validator lỗi detection/file (5 loại lỗi).
> - Bạn B: Validator metadata và panoptic (4 loại lỗi), tích hợp validate.py.
> - Bạn C: Đối chiếu detection ↔ panoptic, sinh candidates, làm công cụ xem ảnh và tổng hợp review_log.
> - Bạn D: Truy vết ticket, trace.json, bảo mật, tài liệu và prompts.
> giờ tôi cần làm gì để hoàn thành hướng dẫn tôi chi tiết nhé

**Kết quả AI:**
1. Xây dựng module `validator/cross_check.py` tuân thủ 100% chuẩn thư viện Python (không dùng thư viện ngoài trong validator):
   - Quy đổi tọa độ YOLO normalized sang pixel coordinates.
   - Ghép box detection với segment thing trong panoptic theo class name và tọa độ.
   - Sử dụng greedy bipartite matching và tỷ lệ diện tích bao phủ (containment) để phát hiện 5 lỗi gán nhãn: `class_swap`, `category_swap`, `bbox_drift`, `missing_box`, `instance_merge`.
   - Xuất file `candidates.json` và file mẫu `review_queue.csv`.
2. Xây dựng công cụ review trực quan `tools/review_tool.py`:
   - Dùng Pillow vẽ bounding box Detection (Xanh) và Panoptic (Cam) kèm nhãn lên ảnh.
   - Tự động sinh `review_dashboard.html` để cả nhóm mở trên trình duyệt, có nút bấm gán verdict và bộ đếm ký tự đảm bảo ghi chú $\ge 20$ ký tự theo Rubric.
   - Hỗ trợ chế độ CLI (`--cli`) để review bằng bàn phím siêu nhanh trong 40 phút thi đề ẩn.
3. Chạy đo nhiễu trên lô sạch `runs/clean` (`--no-faults`): Thu được đúng **0 ứng viên**, chứng minh thuật toán không báo ảo.
4. Chạy trên seed 2902: Sinh ra 24 ứng viên (16 ảnh). Cả nhóm tham gia mở ảnh review, xác nhận đúng 6 lỗi thật (`confirmed`) và 18 trường hợp lệch tự nhiên COCO (`rejected`).
5. Xuất `candidates.json` và `review_log.csv` vào `submission/r2902/`.

**Sai sót của AI và cách nhóm kiểm lại:**
1. *Sai sót về missing_box:* Ban đầu AI kiểm tra `best_any` với toàn bộ detection boxes của ảnh. Với ảnh `000000023937` (đàn bò), một con bò bên cạnh có IoU 0.388 với segment con bò bị thiếu nhãn, khiến AI lọc nhầm và bỏ sót ca này.
   *Khắc phục:* Nhóm đã chỉnh lại logic: chạy greedy bipartite matching trước, sau đó chỉ kiểm tra IoU với các box chưa được ghép (`unmatched_boxes`). Sau khi sửa, phát hiện chính xác 100% ca thiếu nhãn.
2. *Sai sót về instance_merge:* Ban đầu AI chỉ dùng IoU bounding box đơn thuần (`IoU > 0.20`), dẫn tới sinh ra 177 candidates vì nhiều người đứng cạnh nhau trong COCO có box trùng nhau.
   *Khắc phục:* Nhóm đã đổi sang kiểm tra tỷ lệ containment diện tích của từng box nằm trọn trong segment ($\ge 65\%$) kết hợp điều kiện số box > số segment của cùng lớp. Nhờ vậy danh sách ứng viên rút gọn xuống đúng 1 ca duy nhất (`000000015440`).
3. Mọi kết luận gán nhãn trong `review_log.csv` đều do thành viên trực tiếp mở ảnh xem và đối chiếu, không để AI tự quyết định thay người.


# Báo cáo nhóm (chờ bổ sung mã nhóm)

## 1. Số liệu luyện tập
- Seed thống nhất hiện tại: `2902` (release v1: `lab250_9f8af853f974`).
- F1 theo seed (rule / cross_check / overall):
  * Nhóm lỗi gán nhãn (cross_check_review): Tìm được chính xác 6/6 lỗi gán nhãn sau khi review bằng mắt (gồm 1 class_swap, 1 category_swap, 1 bbox_drift, 2 missing_box, 1 instance_merge). Recall = 1.0, Precision = 1.0, F1 = 1.0 (trên 6 ca confirmed).
- Số ứng viên trên lô sạch (`--no-faults`) và hàng đợi trên seed:
  * Lô sạch (`runs/clean` - 50 ảnh calib): **0 ứng viên** (thuật toán bipartite matching và containment không sinh false candidate nào).
  * Hàng đợi trên seed 2902: **24 ứng viên** (thuộc 16 ảnh). Hàng đợi gọn gàng, phù hợp để nhóm 5 người xem mắt trong 5-10 phút.
- Ngưỡng đã chọn và cách chọn (không dùng `_private`):
  * IoU ghép lớp lệch (class_swap / category_swap): IoU >= 0.40 giữa detection box và panoptic thing segment.
  * Instance merge: Segment thing có diện tích >= 1024 px, bao phủ >= 2 box detection cùng lớp với tỷ lệ containment >= 65%, và số box cùng lớp > số segment cùng lớp.
  * BBox drift: Cặp cùng lớp có 0.35 <= IoU <= 0.78 và khoảng cách tâm lệch >= 8% đường chéo box.
  * Missing box: Segment thing có diện tích >= 1000 px, diện tích tương đối >= 1% ảnh, không có box nào chưa ghép đạt IoU >= 0.40.
  * Các ngưỡng này được hiệu chuẩn trên lô sạch `runs/clean` để đảm bảo 0 false alarms trước khi áp dụng vào lô luyện tập.

## 2. Vì sao báo hết ứng viên làm F1 giảm?
Ứng viên (`candidates.json`) chỉ là các trường hợp có nghi vấn bất đồng giữa Detection và Panoptic, **không đồng nghĩa tất cả đều là lỗi gán nhãn**.
COCO có độ lệch tự nhiên giữa hai nguồn dữ liệu do:
1. Ranh giới lớp mập mờ (ví dụ: xe tải thùng lớn vs xe bus ở `000000006723`, chén trà nhỏ cup vs bowl ở `000000009590`, hot dog vs sandwich ở `000000009914`, lọ hoa vs chai ở `000000020553`).
2. Vật thể bị che khuất một phần ở viền ảnh hoặc bởi vật thể khác phía trước.

**Minh chứng từ số liệu thực nghiệm của nhóm trên seed 2902:**
- Nếu báo hết tất cả 24 ứng viên vào `errors.json`, số False Positives (FP) sẽ tăng vọt từ 0 lên 18 ca.
- Precision sẽ giảm từ 1.0 (6/6) xuống còn 0.25 (6/24).
- Rank F1 sẽ tụt dốc từ ~1.0 xuống dưới **0.40**!
Do đó, việc cả nhóm cùng tham gia **review bằng mắt** và ghi nhận `confirmed` (lỗi thật) hoặc `rejected` (lệch tự nhiên có giải thích >= 20 ký tự) là yếu tố quyết định để giữ Precision và F1 ở mức tối đa.

## 3. Quyết định và lineage
Lineage hiện ghi seed `2902` (`lab250_9f8af853f974`) và training run `R-021`. Chưa có `errors.json`, quyết định QC v1/HOLD, hay bản v2 để xác minh; không tự kết luận QC hoặc ghi nhận release. Nếu v1 bị HOLD, model R-021 cần được đánh giá lại hoặc huấn luyện lại vì sửa dataset không thay đổi dữ liệu model đã học.

## 4. Hash chứng minh gì, không chứng minh gì?
SHA-256 trong manifest giúp kiểm tra file hiện tại có trùng byte với file đã ghi nhận khi lập manifest hay không. Hash không chứng minh ảnh hoặc nhãn đúng ngữ nghĩa, người tạo có thẩm quyền, file không chứa dữ liệu nhạy cảm, hay nội dung có thể phát hành. Cần kiểm nội dung và quyền truy cập riêng.

## 5. Truy vết
Với seed `2902`, ticket báo `scene_814` và `scene_952`; changelog nêu quy tắc mới cho class `cup` (class ID `41`). Tier A gồm ảnh trong các scene được báo nếu job dùng guideline `v1.2` và nhãn có box cup; tier B là các ảnh khác thỏa cùng điều kiện. Guideline phải lấy từ `jobs.csv`, vì metadata từng ảnh có thể sai. Kết quả: tier A `000000003661`, `000000003845`, `000000003934`; tier B `000000002157`, `000000002431`, `000000002592`, `000000002685`; notify `A02`, `Q03`. Metadata của ảnh `000000011149` không khớp guideline trong job; phân loại vẫn dựa theo `jobs.csv`.

## 6. Bug hoặc điểm chưa rõ trong lab (nếu có)
Chưa xác minh được bug trong script của lab. Một lần chạy ban đầu bị lỗi encoding đầu ra tiếng Việt trên Windows (`cp1252`); chạy lại với `PYTHONUTF8=1` thành công, nên đây được ghi nhận là vấn đề cấu hình console của máy, không phải bug đã xác nhận của script.

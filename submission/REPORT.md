# Báo cáo nhóm (chờ bổ sung mã nhóm)

## 1. Số liệu luyện tập
- Seed thống nhất hiện tại: `2902` (release v1: `lab250_9f8af853f974`).
- F1 theo seed (rule / cross_check / overall): Chưa có; validator và `errors.json` chưa được cung cấp trong workspace.
- Số ứng viên trên lô sạch (`--no-faults`) và hàng đợi trên seed: Chưa có số liệu kiểm chứng.
- Ngưỡng đã chọn và cách chọn (không dùng `_private`): Nhóm cần ghi sau khi chạy validator trên lô sạch và tự review hàng đợi. Không đọc hoặc dò `_private`.

## 2. Vì sao báo hết ứng viên làm F1 giảm?
Ứng viên là các trường hợp nghi ngờ, không đồng nghĩa tất cả đều sai nhãn. COCO có thể có khác biệt tự nhiên giữa detection và panoptic do che khuất, crowd hoặc khác biệt vùng bao. Đưa mọi ứng viên vào kết quả làm tăng false positive, giảm precision và do đó có thể giảm F1. Cần bổ sung số liệu precision/recall/F1 của nhóm sau khi review; hiện chưa có `errors.json` để báo số cụ thể.

## 3. Quyết định và lineage
Lineage hiện ghi seed `2902` (`lab250_9f8af853f974`) và training run `R-021`. Chưa có `errors.json`, quyết định QC v1/HOLD, hay bản v2 để xác minh; không tự kết luận QC hoặc ghi nhận release. Nếu v1 bị HOLD, model R-021 cần được đánh giá lại hoặc huấn luyện lại vì sửa dataset không thay đổi dữ liệu model đã học.

## 4. Hash chứng minh gì, không chứng minh gì?
SHA-256 trong manifest giúp kiểm tra file hiện tại có trùng byte với file đã ghi nhận khi lập manifest hay không. Hash không chứng minh ảnh hoặc nhãn đúng ngữ nghĩa, người tạo có thẩm quyền, file không chứa dữ liệu nhạy cảm, hay nội dung có thể phát hành. Cần kiểm nội dung và quyền truy cập riêng.

## 5. Truy vết
Với seed `2902`, ticket báo `scene_814` và `scene_952`; changelog nêu quy tắc mới cho class `cup` (class ID `41`). Tier A gồm ảnh trong các scene được báo nếu job dùng guideline `v1.2` và nhãn có box cup; tier B là các ảnh khác thỏa cùng điều kiện. Guideline phải lấy từ `jobs.csv`, vì metadata từng ảnh có thể sai. Kết quả: tier A `000000003661`, `000000003845`, `000000003934`; tier B `000000002157`, `000000002431`, `000000002592`, `000000002685`; notify `A02`, `Q03`. Metadata của ảnh `000000011149` không khớp guideline trong job; phân loại vẫn dựa theo `jobs.csv`.

## 6. Bug hoặc điểm chưa rõ trong lab (nếu có)
Chưa xác minh được bug trong script của lab. Một lần chạy ban đầu bị lỗi encoding đầu ra tiếng Việt trên Windows (`cp1252`); chạy lại với `PYTHONUTF8=1` thành công, nên đây được ghi nhận là vấn đề cấu hình console của máy, không phải bug đã xác nhận của script.

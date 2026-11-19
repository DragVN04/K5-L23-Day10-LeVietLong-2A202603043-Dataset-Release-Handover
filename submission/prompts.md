# Dùng AI

| # | Ai dùng | Công cụ | Prompt (tóm tắt) | AI sai ở đâu | Nhóm kiểm lại thế nào |
|---|---|---|---|---|---|
| 1 | Thành viên phụ trách | Copilot SDK trong VS Code | Đọc yêu cầu, tạo lô seed `2902`, tính trace và kiểm tra một ảnh ứng viên có khuôn mặt. | Lần chạy đầu dừng ở thông báo tiếng Việt do Windows dùng `cp1252`. AI chỉ hỗ trợ kiểm tra ảnh; nhóm vẫn phải xác nhận trực tiếp theo quy định bài lab. | Chạy lại với `PYTHONUTF8=1`; xác nhận delivery có 250 ảnh và 250 mask. Tính trace từ ticket, changelog, `jobs.csv`, labels và manifest; dùng guideline trong `jobs.csv`, không đọc `_private/`. Mở `000000001000.jpg`, ghi nhận nhiều khuôn mặt rõ và yêu cầu thành viên xác nhận trước khi merge. |

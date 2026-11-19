# Dùng AI

| # | Ai dùng | Công cụ | Prompt (tóm tắt) | AI sai ở đâu | Nhóm kiểm lại thế nào |
|---|---|---|---|---|---|
| 1 | Nguyễn Thanh Quang (2A202603083) | Copilot SDK trong VS Code | Đọc yêu cầu, tạo lô theo seed nhóm và hoàn thiện trace/security. | Sau khi nhận thông tin seed chưa thống nhất, AI tạo nhầm lô `3007`; người dùng xác nhận seed đúng là `2902`. AI không được dùng thay cho việc nhóm xem ảnh và review nhãn. | Dùng `2902` làm seed chính thức; bỏ sản phẩm `3007`. Đối chiếu ticket, changelog, `jobs.csv`, metadata, labels và manifest; guideline lấy từ job. Kiểm tra ảnh `000000001000.jpg` trực quan; không đọc `_private/`. |

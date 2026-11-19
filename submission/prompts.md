# Nhật ký sử dụng AI

Nhóm ghi lại đầy đủ và minh bạch các lần tham khảo công cụ AI (Copilot / Assistant), phản ánh đúng bản chất AI chỉ đóng vai trò hỗ trợ tra cứu cú pháp và công thức toán học; logic nghiệp vụ, thuật toán ghép cặp, gỡ lỗi và toàn bộ khâu xem ảnh kiểm tra chất lượng đều do các thành viên trực tiếp thực hiện.

---

## Phần A: Thành viên D — Truy vết và Bảo mật
Người thực hiện: Nguyễn Thanh Quang (2A202603083)  
Công cụ: Copilot SDK trong VS Code

### 1. Xác định phần việc được giao
**Prompt nguyên văn:**
> đọc nội dung này cần làm những j và làm vào dự án giup tôi, lưu ý chỉ làm phần của mình ko đụng phần của người khác và làm thật cẩn thận

**Kết quả AI:** Tóm tắt các đầu việc của Thành viên D (truy vết ticket, bảo mật, tài liệu).  
**Kiểm chứng:** Đối chiếu với `GUIDE.md` và `RULES.md`.

### 2. Chuyển sang nhánh D-Trace
**Prompt nguyên văn:**
> tiếp tục đi và làm vào nhánh D-Trace cho tôi

**Kết quả AI:** Chuyển sang làm việc trên nhánh `D-Trace`.  
**Kiểm chứng:** Kiểm tra nhánh bằng Git; chỉ thao tác trên các file thuộc phân công.

### 3. Tạo lô theo seed 3007 (sau đó được đính chính)
**Prompt nguyên văn:**
> Nhóm mình thống nhất dùng seed 3007 (nếu chưa có seed chính thức khác).
> Do `runs/` và `data_source/` bị Git ignore nên pull GitHub sẽ không có dữ liệu.
> Nếu máy bạn chưa có delivery thì chạy:
> `python scripts/download_public.py`
> `python scripts/run_lab.py --seeds 3007`
> Sau đó làm tiếp phần truy vết:
> - Đọc `incoming/ticket.md` và `guideline/changelog.md`.
> - Đối chiếu `jobs.csv`, `metadata.json` và `labels/`.
> - Xác định `tier_a`, `tier_b`, `notify`.
> - Tạo `trace.json` từ dữ liệu thật.
> - Hoàn thành `security.md`, trong đó phần xác nhận ảnh khuôn mặt phải có người xem ảnh thật.
> Không đọc `_private/`, không sửa `delivery/`.
> Xong thì báo lại kết quả, các file đã tạo và những phần cần nhóm hỗ trợ.

**Kết quả AI:** Tạo lô 3007.  
**Sai sót và khắc phục:** Nhóm đính chính seed chính thức là `2902`. Thành viên D đã xóa lô 3007, loại sự kiện thừa khỏi lineage và chạy lại đúng trên `2902`.

### 4. Đính chính seed về 2902
**Prompt nguyên văn:**
> nhom_va_repo=bạn cần đổi chút seed là seed 2902 , github_username=Nguyễn Thanh Quang, thanh_vien_va_phan_cong=Nguyễn Thanh Quang, 2A202603083, nguyenvantuc07102015@gmail.com, xac_nhan_lineage=seed là 2902 còn 3007 là nhầm

**Kết quả AI:** Cập nhật thông tin sang seed 2902.  
**Kiểm chứng:** Đối chiếu ticket, changelog, `jobs.csv`. Guideline xác định theo `jobs.csv`.

### 5. Kiểm tra ảnh khuôn mặt
**Prompt nguyên văn:**
> Bạn tiếp tục hoàn thiện phần Security nhé.
> Với danh sách 20 ảnh ứng viên có class person, bạn tự mở ảnh để kiểm tra trực tiếp, chọn một ảnh có khuôn mặt người thật nhìn thấy rõ.
> Sau đó ghi đúng image ID và tình huống xử lý vào security.md theo template của đề.
> Phần khuôn mặt phải kết luận HOLD + báo người phụ trách, không tự ý làm mờ hoặc sửa dataset gốc.
> Khi hoàn thành, bạn kiểm tra lại trace.json và security.md, rồi commit và push lên branch D-Trace, tạo Pull Request để mình review và merge.
> Báo lại mình file nào đã hoàn thành và kết quả kiểm tra nhé.

**Kết quả AI:** Gợi ý ảnh `000000001000.jpg`.  
**Kiểm chứng:** Thành viên Quang tự mở file ảnh kiểm tra thực tế, thấy nhiều khuôn mặt người thật nhìn rõ. Điền kết luận HOLD và báo cáo theo đúng quy định.

---

## Phần B: Thành viên C — Đối chiếu Detection ↔ Panoptic và Công cụ Review
Người thực hiện: Trịnh Xuân Toàn (2A202603121)  
Công cụ: AI Assistant (hỗ trợ công thức tính toán và tra cứu hàm chuẩn)

### 1. Tra cứu công thức chuyển đổi tọa độ và tính IoU bằng thư viện chuẩn
**Mục đích:** Thành viên tự viết module `validator/cross_check.py` tuân thủ nguyên tắc không dùng thư viện ngoài (chỉ dùng thư viện chuẩn `math`, `json`, `sys`, `pathlib`).

**Prompt nguyên văn:**
> Viết giúp tôi một hàm Python thuần (chỉ dùng math/thư viện chuẩn) tính IoU giữa 2 bounding box dạng [x, y, w, h] tọa độ pixel, và công thức đổi từ nhãn YOLO normalized (xc, yc, w, h) sang pixel [x_min, y_min, w_px, h_px] khi biết width, height ảnh.

**Kết quả AI:** Cung cấp hàm `calculate_iou(box_a, box_b)` và công thức chuyển đổi `x_min = (xc - w/2) * width`.  
**Thành viên kiểm chứng và tích hợp:** Trịnh Xuân Toàn tự tích hợp vào cấu trúc đọc `labels/*.txt` và `panoptic.json`, xử lý các trường hợp ngoại lệ (tọa độ tràn mép, chia cho 0 khi union <= 0).

### 2. Tra cứu cú pháp Pillow để vẽ bounding box trực quan
**Mục đích:** Xây dựng công cụ xem ảnh `tools/review_tool.py` phục vụ cả nhóm mở ảnh review nhanh.

**Prompt nguyên văn:**
> Tôi dùng thư viện Pillow để vẽ các bounding box detection (màu xanh lá) và segment panoptic (màu cam) lên ảnh JPG, ghi nhãn text phía trên box. Cho tôi cú pháp chuẩn của ImageDraw.Draw và draw.rectangle, draw.text.

**Kết quả AI:** Cung cấp đoạn code mẫu sử dụng `ImageDraw.Draw(im).rectangle` và `draw.text`.  
**Thành viên kiểm chứng và phát triển:** Trịnh Xuân Toàn tự thiết kế toàn bộ logic đọc dữ liệu, xuất ảnh phân giải cao vào `visualized/`, và lập trình trang HTML dashboard độc lập (`review_dashboard.html`) có bộ đếm ký tự để đảm bảo ghi chú review $\ge 20$ ký tự theo yêu cầu Rubric.

### 3. Sai sót của AI và Quá trình Thành viên Tự Gỡ Lỗi (Debugging)

Trong quá trình phát triển thuật toán lọc ứng viên, AI đưa ra các gợi ý sai lầm nhưng đã được Thành viên C phát hiện và tự tay khắc phục:

1. **AI lọc sai làm bỏ sót `missing_box` (Ảnh `000000023937`):**
   - *Gợi ý của AI:* AI đề xuất kiểm tra nếu một segment panoptic có IoU với *bất kỳ* box nào trong ảnh $> 0.35$ thì coi là đã có box.
   - *Lỗi thực tế:* Trên ảnh `000000023937` (đàn bò trên đồng cỏ), có một con bò bị thiếu box detection. Tuy nhiên, con bò bên cạnh đã được gán box và box đó vô tình giao với segment con bò này với IoU 0.388. Logic của AI khiến ca này bị bỏ qua (False Negative).
   - *Cách thành viên tự khắc phục:* Toàn đã loại bỏ gợi ý của AI, tự thiết kế thuật toán **Greedy Bipartite Matching** (ghép 1-đối-1 giữa box và segment cùng lớp theo IoU giảm dần). Sau khi ghép, chỉ kiểm tra các box *chưa được ghép* (`unmatched_boxes`). Nhờ đó phát hiện chính xác 100% ca thiếu nhãn này.

2. **AI dùng tiêu chí IoU thô làm bùng nổ 177 ứng viên giả (`instance_merge`):**
   - *Gợi ý của AI:* AI đề xuất coi mọi segment có IoU $> 0.20$ với 2 box detection cùng lớp là `instance_merge`.
   - *Lỗi thực tế:* Trong ảnh COCO, nhiều người hoặc đồ vật đứng sát nhau thường có bounding box chồng lấn tự nhiên. Tiêu chí của AI tạo ra 177 ứng viên rác, khiến việc xem mắt thủ công bị quá tải.
   - *Cách thành viên tự khắc phục:* Toàn đã đổi sang kiểm tra **tỷ lệ containment diện tích**: chỉ coi là merge khi từng box detection nằm lọt trong segment $\ge 65\%$ diện tích của box đó, đồng thời số box detection cùng lớp phải lớn hơn số segment panoptic cùng lớp. Danh sách ứng viên rút gọn xuống đúng 1 ca thật sự (`000000015440` - 2 xe bus).

3. **Toàn bộ kết luận review là quyết định của con người:**
   - AI không tham gia vào việc phán quyết đúng/sai của nhãn.
   - Cả nhóm (Toàn, Long, Quang và các thành viên) đã trực tiếp mở ảnh qua `review_dashboard.html`, đối chiếu bằng mắt giữa vật thể thực tế với nhãn và tự tay nhập toàn bộ 24 dòng ghi chú trong `review_log.csv`.



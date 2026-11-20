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

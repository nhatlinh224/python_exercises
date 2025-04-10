import re


def word_counter():
    """
    Đếm số lần xuất hiện của từng từ trong file văn bản người dùng nhập vào.

    Chức năng:
    - Nhập đường dẫn file .txt từ bàn phím
    - Chuyển nội dung sang chữ thường
    - Loại bỏ các ký tự không phải chữ cái (giữ lại khoảng trắng)
    - Tách văn bản thành danh sách các từ
    - Đếm số lần xuất hiện từng từ và in ra kết quả
    """
    # 🔹 Nhập đường dẫn tới file từ người dùng
    file_path = input("🔍 Nhập đường dẫn đến file .txt: ").strip()

    # 🔹 Mở và đọc nội dung file
    with open(f"{file_path}", 'r', encoding='utf-8') as file:
        content = file.read()

    # 🔹 Tiền xử lý: chuyển về chữ thường và loại bỏ ký tự không phải chữ cái
    content = content.lower()
    content = re.sub(r'[^a-zA-Z\s]', '', content)

    # 🔹 Tách văn bản thành danh sách từ
    words = content.split()

    # 🔹 Khởi tạo từ điển để đếm số lần xuất hiện
    diction = {}
    for value in words:
        if value in diction:
            diction[value] += 1
        else:
            diction[value] = 1

    # 🔹 In kết quả đếm từ
    print(f"Số lần các từ xuất hiện: {diction}")

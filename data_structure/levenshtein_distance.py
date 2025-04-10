def levenshtein_distance(source, target):
    m = len(source)
    n = len(target)

    # ✅ Khởi tạo ma trận D có kích thước (m+1) x (n+1), tất cả phần tử ban đầu là 0
    D = []
    for i in range(m + 1):
        row = []
        for j in range(n + 1):
            row.append(0)
        D.append(row)

    # ✅ Điền giá trị cho hàng đầu tiên và cột đầu tiên (cơ sở quy hoạch động)
    for i in range(m + 1):
        D[i][0] = i  # chi phí xóa từng ký tự từ source để thành rỗng
    for j in range(n + 1):
        D[0][j] = j  # chi phí chèn từng ký tự vào source để thành target

    # ✅ Tính toán các giá trị còn lại trong ma trận
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if source[i - 1] == target[j - 1]:
                substitution_cost = 0  # không cần thay thế
            else:
                substitution_cost = 1  # cần thay thế

            D[i][j] = min(
                D[i - 1][j] + 1,                     # Xóa
                D[i][j - 1] + 1,                     # Chèn
                D[i - 1][j - 1] + substitution_cost  # Thay thế
            )

    # ✅ Giá trị khoảng cách Levenshtein là ô dưới cùng bên phải của ma trận
    return D[m][n]

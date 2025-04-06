def md_nre():
    """
    Hàm nhập input từ người dùng và tính MD_nRE (Mean Difference of nth Root Error)
    cho một cặp y và y_hat.

    Công thức:
        MD_nRE = |y^(1/n) - y_hat^(1/n)| ^ p

    Input:
        - y: giá trị thật (float)
        - y_hat: giá trị dự đoán (float)
        - n: căn bậc (int > 0)
        - p: bậc hàm loss (float > 0)

    Output:
        - In kết quả MD_nRE ra màn hình
    """
    y = float(input("Nhập giá trị y (ground truth): "))
    y_hat = float(input("Nhập giá trị y_hat (predict): "))
    n = int(input("Nhập căn bậc n (n > 0): "))
    p = float(input("Nhập bậc p của hàm loss (p > 0): "))

    y_root = y ** (1 / n)
    y_hat_root = y_hat ** (1 / n)
    loss = abs(y_root - y_hat_root) ** p

    print(f"\n✅ Kết quả MD_nRE: {loss}")



import math


def taylor_series():
    try:
        x = float(input("Nhập giá trị x (đơn vị: radian): "))
    except ValueError:
        print("❌ x phải là một số thực")
        return

    func = input("Nhập tên hàm (sin, cos, sinh, cosh): ").lower()
    n_str = input("Nhập số lần lặp (n > 0): ")

    if not n_str.isnumeric() or int(n_str) <= 0:
        print("❌ n phải là số nguyên dương lớn hơn 0")
        exit()

    n = int(n_str)
    result = 0

    for i in range(n):
        if func == "sin":
            term = ((-1) ** i) * (x ** (2 * i + 1)) / math.factorial(2 * i + 1)
        elif func == "cos":
            term = ((-1) ** i) * (x ** (2 * i)) / math.factorial(2 * i)
        elif func == "sinh":
            term = (x ** (2 * i + 1)) / math.factorial(2 * i + 1)
        elif func == "cosh":
            term = (x ** (2 * i)) / math.factorial(2 * i)
        else:
            print("⚠️ Hàm không hợp lệ. Vui lòng chọn: sin, cos, sinh, cosh.")
            return
        result += term

    print(f"\n✅ Kết quả gần đúng của {func}3.14 là: {result}")




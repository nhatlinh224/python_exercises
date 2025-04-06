import math


def is_number(x):
    """
    Kiểm tra xem giá trị đầu vào có thể chuyển sang kiểu float không.

    Args:
        x (str): Giá trị nhập vào.

    Returns:
        True nếu là số, ngược lại trả về chuỗi thông báo lỗi.
    """
    try:
        float(x)
    except ValueError:
        return "Không hợp lệ, x phải là một số."
    return True


def activation_function():
    """
    Hàm xử lý giá trị x thông qua một trong 3 hàm activation:
    - sigmoid
    - relu
    - elu

    Người dùng nhập x và tên activation function.
    Kết quả f(x) sẽ được in ra theo format: activation: f(x) = result
    """
    x = input("Nhập giá trị của x: ")

    if is_number(x) is not True:
        print(is_number(x))
        return

    x = float(x)
    function_name = input(
        "Nhập tên activation function (sigmoid, relu, elu): ").lower()

    print(f"x = {x}")

    if function_name == "sigmoid":
        result = 1 / (1 + math.exp(-x))
        print(f"sigmoid: f({x}) = {result}")
        return

    if function_name == "relu":
        result = max(0, x)
        print(f"relu: f({x}) = {result}")
        return

    if function_name == "elu":
        alpha = 0.1
        result = x if x > 0 else alpha * (math.exp(x) - 1)
        print(f"elu: f({x}) = {result}")
        return

    print("Hàm activation không hợp lệ. Vui lòng chọn: sigmoid, relu, hoặc elu.")




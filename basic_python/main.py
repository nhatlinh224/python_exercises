from activation_function import activation_function
from f1_score_calculator import f1_score_calculator
from regression_loss import regression_loss
from taylor_series import taylor_series
from mean_diff_nth_root_error import md_nre


def main():
    while True:
        print("\n--- MENU CHỌN BÀI ---")
        print("1. F1-Score")
        print("2. Activation Function")
        print("3. Regression Loss (MAE, MSE, RMSE)")
        print("4. Taylor Series (sin, cos, sinh, cosh)")
        print("5. Mean Difference of nth Root Error")
        print("0. Thoát")

        choice = input("Chọn bài (0-5): ")
        if choice == "1":
            f1_score_calculator()
        elif choice == "2":
            activation_function()
        elif choice == "3":
            regression_loss()
        elif choice == "4":
            taylor_series()
        elif choice == "5":
            md_nre()
        elif choice == "0":
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")


if __name__ == "__main__":
    main()

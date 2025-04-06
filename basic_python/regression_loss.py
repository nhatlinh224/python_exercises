import math
import random


def regression_loss():
    """
    Hàm cho phép người dùng chọn loss function (MAE, MSE, RMSE),
    tự sinh ngẫu nhiên các cặp predict - target để tính loss tương ứng.
    """
    num_samples = input("Nhập số lượng sample (num_samples): ")

    if not num_samples.isnumeric():
        print("number of samples must be an integer number")
        return

    num_samples = int(num_samples)

    loss_name = input("Nhập loss name (MAE, MSE, hoặc RMSE): ").upper()

    print(f"\nLoss function: {loss_name}")
    print(f"{'Sample':<10} {'Predict':<10} {'Target':<10} {'Loss':<10}")

    total_loss = 0

    for i in range(num_samples):
        predict = random.uniform(0, 10)
        target = random.uniform(0, 10)

        if loss_name == "MAE":
            loss = abs(predict - target)
        elif loss_name in ["MSE", "RMSE"]:
            loss = (predict - target) ** 2

        total_loss += loss
        print(f"sample-{i:<4}  {predict:<10.2f} {target:<10.2f} {loss:<10.4f}")

    if loss_name == "RMSE":
        final_loss = math.sqrt(total_loss / num_samples)
    else:
        final_loss = total_loss / num_samples

    print(f"\n➤ Tổng {loss_name}: {final_loss:.4f}")




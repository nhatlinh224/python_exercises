def f1_score_calculator():
    """
    Tính toán và in ra Precision, Recall và F1-Score của một mô hình classification.

    Hàm yêu cầu người dùng nhập vào 3 giá trị:
    - tp (True Positives)
    - fp (False Positives)
    - fn (False Negatives)

    Điều kiện:
    - Các giá trị tp, fp, fn phải là số nguyên (int)
    - Tất cả phải lớn hơn 0

    Output:
    - In ra Precision, Recall và F1-Score dưới dạng số thực
    """
    tp = int(input("Nhập giá trị của tp: "))
    if not isinstance(tp, int):
        print("tp must be int")
        raise ValueError

    fp = int(input("Nhập giá trị của fp: "))
    if not isinstance(fp, int):
        print("fp must be int")
        raise ValueError

    fn = int(input("Nhập giá trị của fn: "))
    if not isinstance(fn, int):
        print("fn must be int")
        raise ValueError

    if tp <= 0 or fp <= 0 or fn <= 0:
        print("tp and fp and fn must be greater than zero")
        return

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * (precision * recall) / (precision + recall)

    print(f"Giá trị precision: {precision}")
    print(f"Giá trị của recall: {recall}")
    print(f"Giá trị f1_score: {f1_score}")

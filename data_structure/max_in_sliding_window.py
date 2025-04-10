def max_in_sliding_window(num_list, k):
    """
    Trả về danh sách các giá trị lớn nhất trong mỗi sliding window kích thước k.

    Parameters:
    - num_list (list of int): Danh sách các số nguyên đầu vào.
    - k (int): Kích thước cửa sổ trượt.

    Returns:
    - list of int: Danh sách các giá trị lớn nhất tương ứng với mỗi cửa sổ trượt.
    """
    result = []
    for i in range(len(num_list) - k + 1):
        sliding_window = num_list[i:i + k]
        result.append(max(sliding_window))
    return result

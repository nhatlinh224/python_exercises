def count_chars():
    """
    Đếm số lần xuất hiện của từng chữ cái trong một từ do người dùng nhập vào.

    Trả về:
        dict: Từ điển với key là ký tự, value là số lần xuất hiện.
    """
    word = input("Nhập từ bạn muốn đếm: ").lower()
    diction = {}

    for char in word:
        if char in diction:
            diction[char] += 1
        else:
            diction[char] = 1

    return diction

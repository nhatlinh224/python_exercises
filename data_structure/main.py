from count_chars import count_chars
from levenshtein_distance import levenshtein_distance
from max_in_sliding_window import max_in_sliding_window
from word_counter import word_counter

def main():
    while True:
        print("\n--- MENU CHỌN BÀI (Data Structure) ---")
        print("1. Đếm ký tự")
        print("2. Tính khoảng cách Levenshtein")
        print("3. Max trong Sliding Window")
        print("4. Đếm từ trong văn bản")
        print("0. Thoát")

        choice = input("Chọn bài (0-4): ")

        if choice == "1":
            count_chars()
        elif choice == "2":
            levenshtein_distance()
        elif choice == "3":
            max_in_sliding_window()
        elif choice == "4":
            word_counter()
        elif choice == "0":
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")

if __name__ == "__main__":
    main()

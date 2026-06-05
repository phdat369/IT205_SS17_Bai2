product_list = [
    "P01-Tai Nghe Bluetooth-550000-4.5",
    "P02-Chuột Không Dây-250000-4.8",
    "P03-Bàn Phím Cơ-850000-4.5"
]
def display_product(products): 
    print("--- DANH SÁCH TEM NHÃN ---")
    for index,item in enumerate(products):
        product = item.split("-")
        print(f"Mã: {product[0]: <10} | Tên: {product[1]: <20} | Giá: {int(product[2]): ,} {"VND": <10}   | Rating: {product[3]}*")
def sort_product(products):
    new_list = sorted(products,key = lambda item: (-float(item.split("-")[3]), int(item.split("-")[2])))
    print("--- SẮP XẾP SẢN PHẨM ---")
    print("Đã sắp xếp thành công! Cập nhật danh sách:")
    for index,item in enumerate(new_list):
        print(f"{index+1}. {item}")
def total_price(products):
    sum = 0
    for item in products:
        price = int(item.split("-")[2])
        sum += price 
    return sum
def main():
    while True:
        choose = input("""============= E-COMMERCE ANALYTICS =============
1. Hiển thị tem nhãn sản phẩm (format_map & F-String)
2. Sắp xếp sản phẩm thông minh (sort key)
3. Tính tổng giá trị kho hàng (reduce)
4. Đóng hệ thống
================================================
Chọn chức năng (1-4): """)
        if choose == "1":
            display_product(product_list)
            print()
        elif choose == "2":
            sort_product(product_list)
            print()
        elif choose == "3":
            print("--- TỔNG GIÁ TRỊ KHO ---")
            print(f"Tổng giá trị các mặt hàng hiện tại là: {total_price(product_list): ,} VND")
            print()
        elif choose == "4":
            print("--- Chương trình kết thúc ---")
            break
        else:
            print("Lựa chọn không hợp lệ")
main()
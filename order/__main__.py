from order.create.create_category import create_categories, random_category
from order.create.create_order import create_order, order
from order.create.create_product import create_product, products
from order.create.create_user import create_user, generate_random_user_data
from order.create.sub_category import create_sub_categories, sub_category_data
from order.export.export_category_data import *
from order.export.export_order_data import *
from order.export.export_product_data import *
from order.export.export_sub_category import *
from order.export.export_user_data import *

action = input(
    "Pick a Number to proceed\n\n (1.) Create User\n\n (2.) Create Product Category\n\n (3.) Create Product Sub Category\n\n (4.) Create Product\n\n (5.) Create Order\n\n (6.) All\n\n Answer:."
)
path = user_csv_file_path[:-8]
if not os.path.isdir(path):
    os.mkdir(path)

if action == str(1):
    print("Create User")
    if __name__ == "__main__":
        num_users_to_create = int(input("Enter a range:. "))
        for _ in range(num_users_to_create):
            user_data = generate_random_user_data()
            create_user(user_data)

elif action == str(2):
    print("Create Product Category")
    if __name__ == "__main__":
        num_users_to_create = int(input("Enter a range:. "))
        for _ in range(num_users_to_create):
            category_data = random_category()
            create_categories(category_data)

elif action == str(3):
    print("Create Sub Category")
    if __name__ == "__main__":
        num_users_to_create = int(input("Enter a range:. "))
        for _ in range(num_users_to_create):
            sub_categorydata = sub_category_data()
            create_sub_categories(sub_categorydata)

elif action == str(4):
    print("Create Product")
    if __name__ == "__main__":
        num_users_to_create = int(input("Enter a range:. "))
        for _ in range(num_users_to_create):
            product_data = products()
            create_product(product_data)

elif action == str(5):
    print("Create Order")
    if __name__ == "__main__":
        num_users_to_create = int(input("Enter a range:. "))
        for _ in range(num_users_to_create):
            order_data = order()
            create_order(order_data)
        date = order_date_module()
        data = order_data(date)
        export_order_data(data, orders_excel_file_path, orders_csv_file_path)


elif action == str(6):
    print("Create all")
    if __name__ == "__main__":
        num_users_to_create = int(input("Enter a range:. "))  # Change this as needed
        for _ in range(num_users_to_create):
            user_data = generate_random_user_data()
            create_user(user_data)
        date = user_date_module()
        data = users_data(date)
        export_user_data(data, user_excel_file_path, user_csv_file_path)

        for _ in range(num_users_to_create):
            category_data = random_category()
            create_categories(category_data)
        data = product_category_data()
        export_category_data(data, category_excel_file_path, category_csv_file_path)

        for _ in range(num_users_to_create):
            sub_categorydata = sub_category_data()
            create_sub_categories(sub_categorydata)
        data = product_sub_category_data()
        export_sub_category_data(
            data, sub_category_excel_file_path, sub_category_csv_file_path
        )

        for _ in range(num_users_to_create):
            product_data = products()
            create_product(product_data)
        data = products_data()
        export_product_data(data, product_excel_file_path, product_csv_file_path)
        for _ in range(num_users_to_create):
            order_data = order()
            create_order(order_data)
        date = order_date_module()
        data = order_data(date)
        export_order_data(data, orders_excel_file_path, orders_csv_file_path)

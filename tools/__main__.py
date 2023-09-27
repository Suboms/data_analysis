from .create_user import generate_random_user_data, create_user
from .create_category import random_category, create_categories
from .sub_category import sub_category_data, create_sub_categories
from .create_product import products, create_product
from .create_order import create_order, order



action = input("Pick a Number to proceed\n\n (1.) Create User\n\n (2.) Create Product Category\n\n (3.) Create Product Sub Category\n\n (4.) Create Product\n\n (5.) Create Order\n\n (6.) All\n\n Answer:.")

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

elif action == str(6):
    print("Create all")
    if __name__ == "__main__":
        num_users_to_create = int(input("Enter a range:. "))  # Change this as needed
        for _ in range(num_users_to_create):
            user_data = generate_random_user_data()
            create_user(user_data)

            category_data = random_category()
            create_categories(category_data)

            sub_categorydata = sub_category_data()
            create_sub_categories(sub_categorydata)

            product_data = products()
            create_product(product_data)

            order_data = order()
            create_order(order_data)

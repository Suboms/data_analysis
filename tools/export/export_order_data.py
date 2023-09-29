from tools.project_path import *
import pandas as pd
import pytz
from datetime import datetime

# Query all the Order objects
orders = Order.objects.all().order_by("?")

orders_excel_file_path = "/home/dubsy/Desktop/Data Analysis/orders.xlsx"
orders_csv_file_path = "/home/dubsy/Desktop/Data Analysis/orders.csv"


def order_date_module():
    order_date = []
    dates = [
        order.date.strftime("%Y-%m-%d %H:%M") if order.date else "" for order in orders
    ]
    for date in dates:
        time_zone = pytz.timezone("Africa/Lagos")
        strip_date = datetime.strptime(date, "%Y-%m-%d %H:%M")
        new_date = strip_date.replace(tzinfo=pytz.utc)
        loc_dt = new_date.astimezone(time_zone)
        final_date = loc_dt.strftime("%Y-%m-%d %H:%M")
        order_date.append(final_date)
    return order_date


def order_data(date):
    order_data = {
        "Customer Name": [
            f"{order.user.first_name} {order.user.last_name}" if order.user else ""
            for order in orders
        ],
        "Custmer Email": [order.user.email if order.user else "" for order in orders],
        "Age": [order.user.age if order.user else "" for order in orders],
        "Age Group": [order.user.age_group if order.user else "" for order in orders],
        "Gender": [order.user.gender if order.user else "" for order in orders],
        "Country": [order.user.country if order.user else "" for order in orders],
        "State": [order.user.state if order.user else "" for order in orders],
        "Product Categories": [
            order.product_categories.name if order.product_categories else ""
            for order in orders
        ],
        "Product Sub Categories": [
            order.product_sub_categories.name if order.product_sub_categories else ""
            for order in orders
        ],
        "Product": [order.product.name if order.product else "" for order in orders],
        "Product Quantity": [
            order.product.quantity if order.product else "" for order in orders
        ],
        "Unit Cost": [
            order.product.unit_cost if order.product else "" for order in orders
        ],
        "Total Unit Cost": [
            order.product.quantity * order.product.unit_cost if order.product else ""
            for order in orders
        ],
        "Unit Price": [order.price if order.price else "" for order in orders],
        "Order Quantity": [order.quantity if order.quantity else "" for order in orders],
        "Total Price": [
            order.total_price if order.total_price else "" for order in orders
        ],
        "Date": [date for date in date],
    }
    return order_data


def export_order_data(data, excel_file_path, csv_file_path):
    df = pd.DataFrame(data)
    df.to_excel(excel_file_path, index=False, sheet_name="Order1")
    df.to_csv(
        csv_file_path,
        index=False,
    )
    print(f"Successfully Exported data to {excel_file_path} and {csv_file_path}")

from tools.project_path import *
import pandas as pd
import pytz
from datetime import datetime

products = Product.objects.all().order_by("?")

product_excel_file_path = "/home/dubsy/Desktop/Data Analysis/product.xlsx"


product_csv_file_path = "/home/dubsy/Desktop/Data Analysis/product.csv"


def products_data():
    product_data = {
        "Name": [product.name if product.name else "" for product in products],
        "Product Category": [
            product.product_categories.name if product.product_categories else ""
            for product in products
        ],
        "Product Sub Category": [
            product.product_sub_categories.name if product.product_sub_categories else ""
            for product in products
        ],
        "Quantity": [
            product.quantity if product.quantity else "" for product in products
        ],
        "Unit Cost": [
            product.unit_cost if product.unit_cost else "" for product in products
        ],
        "Total Cost": [
            product.quantity * product.unit_cost
            if product.quantity and product.unit_cost
            else ""
            for product in products
        ],
        "Unit Price": [
            product.unit_price if product.unit_price else "" for product in products
        ],
    }
    return product_data


def export_product_data(data, excel_file_path, csv_file_path):
    df = pd.DataFrame(data)
    df.to_excel(excel_file_path, index=False, sheet_name="Order1")
    df.to_csv(
        csv_file_path,
        index=False,
    )
    print(f"Successfully Exported data to {excel_file_path} and {csv_file_path}")

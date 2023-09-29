from tools.project_path import *
import pandas as pd
import pytz
from datetime import datetime

product_sub_category = ProductSubCategories.objects.all().order_by("?")

sub_category_excel_file_path = "/home/dubsy/Desktop/Data Analysis/sub_category.xlsx"


sub_category_csv_file_path = "/home/dubsy/Desktop/Data Analysis/sub_category.csv"


def product_sub_category_data():
    product_sub_category_data = {
        "Name": [
            category.name if category.name else "" for category in product_sub_category
        ],
        "Product Category": [
            category.product_categories.name if category.product_categories else ""
            for category in product_sub_category
        ],
    }
    return product_sub_category_data


def export_sub_category_data(data, excel_file_path, csv_file_path):
    df = pd.DataFrame(data)
    df.to_excel(excel_file_path, index=False, sheet_name="Order1")
    df.to_csv(
        csv_file_path,
        index=False,
    )
    print(f"Successfully Exported data to {excel_file_path} and {csv_file_path}")

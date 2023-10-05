from datetime import datetime

import pandas as pd
import pytz

from project_path import *

product_category = ProductCategories.objects.all().order_by("?")

category_excel_file_path = "/home/dubsy/Desktop/Data Analysis/category.xlsx"

category_csv_file_path = "/home/dubsy/Desktop/Data Analysis/category.csv"


def product_category_data():
    product_category_data = {
        "Name": [
            category.name if category.name else "" for category in product_category
        ]
    }
    return product_category_data


def export_category_data(data, excel_file_path, csv_file_path):
    df = pd.DataFrame(data)
    df.to_excel(excel_file_path, index=False, sheet_name="Category Table")
    df.to_csv(
        csv_file_path,
        index=False,
    )
    print(f"Successfully Exported data to {excel_file_path} and {csv_file_path}")

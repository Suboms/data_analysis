import os
from datetime import datetime

import pandas as pd
import pytz

from project_path import *

users = User.objects.all().order_by("?")

user_excel_file_path = "/home/dubsy/Desktop/Data Analysis/user.xlsx"


user_csv_file_path = "/home/dubsy/Desktop/Data Analysis/user.csv"


def user_date_module():
    user_joined_date = []
    date_joined = [
        user.date_joined.strftime("%Y-%m-%d %H:%M") if user.date_joined else ""
        for user in users
    ]
    for date in date_joined:
        time_zone = pytz.timezone("Africa/Lagos")
        striped_date = datetime.strptime(date, "%Y-%m-%d %H:%M")
        new_date = striped_date.replace(tzinfo=pytz.utc)
        loc_user_dt = new_date.astimezone(time_zone)
        final_user_date = loc_user_dt.strftime("%Y-%m-%d %H:%M")
        user_joined_date.append(final_user_date)
    return user_joined_date


def users_data(date):
    user_data = {
        "Username": [user.username if user.username else "" for user in users],
        "First Name": [user.first_name if user.first_name else "" for user in users],
        "Last Name": [user.last_name if user.last_name else "" for user in users],
        "Email": [user.email if user.email else "" for user in users],
        "Age": [user.age if user.age else "" for user in users],
        "Age Group": [user.age_group if user.age_group else "" for user in users],
        "Gender": [user.gender if user.gender else "" for user in users],
        "Country": [user.country if user.country else "" for user in users],
        "State": [user.state if user.state else "" for user in users],
        "Date joined": [date for date in date],
    }
    return user_data


def export_user_data(data, excel_file_path, csv_file_path):

    df = pd.DataFrame(data)
    df.to_excel(excel_file_path, index=False, sheet_name="User Table")
    df.to_csv(
        csv_file_path,
        index=False,
    )
    print(f"Successfully Exported data to {excel_file_path} and {csv_file_path}")

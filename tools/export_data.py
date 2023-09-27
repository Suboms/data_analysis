import csv
from project_path import *

# Query all the Order objects
orders = Order.objects.all()

# Define the CSV file path
csv_file_path = 'orders.csv'

# Write the data to a CSV file
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    # Write the header row
    header = [
        'User',
        'Product Categories',
        'Product Sub Categories',
        'Product',
        'Price',
        'Quantity',
        'Total Price',
        'Date',
        'Slug',
    ]
    csv_writer.writerow(header)
    
    # Write the data rows
    for order in orders:
        csv_writer.writerow([
            order.user.username if order.user else '',
            order.product_categories.name if order.product_categories else '',
            order.product_sub_categories.name if order.product_sub_categories else '',
            order.product.name if order.product else '',
            order.price if order.price else '',
            str(order.quantity),
            str(order.total_price) if order.total_price else '',
            str(order.date) if order.date else '',
            order.slug if order.slug else '',
        ])

print(f"Data from the 'Order' model has been exported to '{csv_file_path}'.")

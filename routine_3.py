# Date: 28/03/2021
# Description: Automate routine task from work
#              Extract the booking and delivery info that is equal to 500k JPY or more than 500k JPY

import csv
import sys
from datetime import datetime
from helper import *

# Revenue
list_revenue_data = compute_revenue_list("cslrevenue.csv")

extract_revenue_list = []

for row in list_revenue_data:
    if int(row[12]) >= 500000: # Index 12th => Revenue
        extract_revenue_list.append(Revenue(row[0], row[9], row[15], row[24], row[12], row[13], row[11]))

for each_data in extract_revenue_list:

    net_sales = compute_net_sales(each_data) # Compute Net sales
    update_net_sales(each_data, net_sales) # Update Net sales

    net_profit_margin_non_percentage = compute_net_profit_margin(each_data) # Compute Net profit margin
    net_profit_margin = format_value_with_percentage(net_profit_margin_non_percentage) # Format value with percentage
    update_net_profit_margin(each_data, net_profit_margin) # Update Net profit margin

# Booking
list_booking_data = compute_booking_list("koreabooking.csv")

extract_booking_list = []

# >= 500,000
for row in list_booking_data:
    if int(row[12]) >= 500000: # Index 12th => Revenue
        extract_booking_list.append(Booking(row[0], row[9], row[24], row[15], row[12], row[13], row[11]))

# Create order number list
all_order_number_list = [each_order_number.get_customer_order_number() for each_order_number in extract_booking_list]
unique_order_number_set = set(all_order_number_list)
unique_order_number_list = list (unique_order_number_set)

# <= -500,000
for row in list_booking_data:
    if int(row[12]) <= -500000: # Index 12th => Revenue
        extract_booking_list.append(Booking(row[0], row[9], row[24], row[15], row[12], row[13], row[11]))   

# List of orders number that is not for currency adjustment
not_currency_adjustment_order_number_list = []

# Find booking data that is not for currency adjustment
for each_order_number in unique_order_number_list: 

    # Create list of booking amount with current order number
    amount_list = [each_booking.get_booking() for each_booking in extract_booking_list if each_order_number == each_booking.get_customer_order_number()] 

    # Sum all booking amount
    total_amount = 0
    for each_amount in amount_list:
        total_amount += int(each_amount)

    # Add the current order to a list if sum amount more than 0
    if total_amount > 0:
        not_currency_adjustment_order_number_list.append(each_order_number)

    total_amount = 0 

# List of booking data that is not for currency adjustment
not_currency_adjustment_booking_data_list = []

# Create new Booking object and add distributor and product model
# with order number that is not for currency adjustment
for each_order_number in not_currency_adjustment_order_number_list:
    new_booking_data_non_currency_adjustment(each_order_number, extract_booking_list, not_currency_adjustment_booking_data_list)

# Add order date for objects from list of booking data that is not for currency adjustment
date_dummy = datetime.strptime("0001/01/01", '%Y/%m/%d').date()

for each_order_number in not_currency_adjustment_order_number_list:
    date = date_dummy
    for current_booking_data in extract_booking_list:
        if current_booking_data.get_customer_order_number() == each_order_number:
            current_order_date = datetime.strptime(current_booking_data.get_order_date(), '%Y/%m/%d').date()
            if current_order_date > date:
                date = current_order_date
    
    for each_booking_data in not_currency_adjustment_booking_data_list:
        if each_booking_data.get_customer_order_number() == each_order_number:
            each_booking_data.set_order_date(date)

# Add booking, cost, unit for objects from list of booking data that is not for currency adjustment
for each_order_number in not_currency_adjustment_order_number_list:
    booking = 0
    booking_cost = 0
    unit = 0
    for each_booking_data in extract_booking_list:
        if each_booking_data.get_customer_order_number() == each_order_number:
            booking += int(each_booking_data.get_booking())
            booking_cost += int(each_booking_data.get_booking_cost())
            unit += int(each_booking_data.get_unit_booking())
    

    for each_booking_data in not_currency_adjustment_booking_data_list:
        if each_order_number == each_booking_data.get_customer_order_number():
            each_booking_data.set_booking(booking)
            each_booking_data.set_booking_cost(booking_cost)
            each_booking_data.set_unit_booking(unit)

# Compute net profit and net profit margin data
for each_data in not_currency_adjustment_booking_data_list:

    net_sales = compute_net_sales_booking(each_data) # Compute Net sales
    set_net_sales_booking(each_data, net_sales) # Update Net sales

    net_profit_margin_non_percentage = compute_net_profit_margin_booking(each_data) # Compute Net profit margin
    net_profit_margin = format_value_with_percentage(net_profit_margin_non_percentage) # Format value with percentage
    set_net_profit_margin_booking(each_data, net_profit_margin) # Update Net profit margin

# Print all info 
print("\n") 
print("<Revenue>")
for each_booking in extract_revenue_list:
  
    print(f"Distributor:{each_booking.get_distributor()}; Product Model:{each_booking.get_product_model()}; Unit:{each_booking.get_unit_revenue()}; Revenue:{int(each_booking.get_revenue()):,}; Net profit margin revenue:{(each_booking.get_net_profit_margin_revenue())}")

print("\n") 
print("<Booking>")
for each_booking in not_currency_adjustment_booking_data_list:
  
    print(f"Distributor:{each_booking.get_distributor()}; Product Model:{each_booking.get_product_model():<10}; Unit:{each_booking.get_unit_booking()}; Booking:{int(each_booking.get_booking()):,}; Net profit margin booking:{(each_booking.get_net_profit_margin_booking())}")

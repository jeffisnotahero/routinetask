# Date: 28/03/2021
# Description: Automate routine task from work
#              Extract the booking and delivery info that is equal to 500k JPY or more than 500k JPY

import csv
import sys
from datetime import datetime
from helper import *

class Booking:
    """
    Represents the booking data with data member such as 
    distributor, product model, order date,
    customer order number, cost, net sales, profit margin.
    """

    def __init__(self, distributor=None, product_model=None, customer_order_number=None, order_date=None, booking=None, booking_cost=None, unit_booking=None):
        """
        Initialize data members for 
        distributor, product model, order date,
        customer order number, cost, net sales, profit margin.
        """
        self._distributor = distributor
        self._product_model = product_model
        self._order_date = order_date
        self._customer_order_number = customer_order_number
        self._booking = booking
        self._booking_cost = booking_cost
        self._unit_booking = unit_booking
        self._net_sales_booking = 0
        self._net_profit_margin_booking = 0
    
    def __repr__(self):
        """
        Returns the customer order number when printing object
        """
        return self._customer_order_number

    def get_distributor(self):
        """
        Returns distributor data
        """
        return self._distributor

    def get_product_model(self):
        """
        Returns product model data
        """
        return self._product_model

    def get_order_date(self):
        """
        Returns order date data
        """
        return self._order_date

    def get_customer_order_number(self):
        """
        Returns customer order number data
        """
        return self._customer_order_number

    def get_booking(self):
        """
        Returns booking data
        """
        return self._booking

    def get_booking_cost(self):
        """
        Returns booking cost data
        """
        return self._booking_cost
    
    def get_unit_booking(self):
        """
        Returns booking unit data
        """
        return self._unit_booking

    def get_net_profit_margin_booking(self):
        """
        Returns net profit margin booking
        """
        return self._net_profit_margin_booking

    def set_order_date(self, new_order_date):
        """
        Set order date data to a new value
        """
        self._order_date = new_order_date

    def set_booking(self, new_booking):
        """
        Set booking data to a new value
        """
        self._booking = new_booking

    def set_booking_cost(self, new_booking_cost):
        """
        Set booking cost data to a new value 
        """
        self._booking_cost = new_booking_cost
    
    def set_unit_booking(self, new_unit_booking):
        """
        Set unit for booking data to a new value
        """
        self._unit_booking = new_unit_booking

class Revenue:
    """
    Represents the revenue data with data member such as 
    distributor, product model, order date,
    customer order number, cost, net sales, profit margin.
    """

    def __init__(self, distributor=None, product_model=None, order_date=None, customer_order_number=None, revenue=None, revenue_cost=None, unit_revenue=None):
        """
        Initialize data member for 
        distributor, product model, order date,
        customer order number, cost, net sales, profit margin.
        """
        self._distributor = distributor
        self._product_model = product_model
        self._order_date = order_date
        self._customer_order_number = customer_order_number
        self._revenue = revenue
        self._revenue_cost = revenue_cost
        self._unit_revenue = unit_revenue
        self._net_sales_revenue = 0
        self._net_profit_margin_revenue = 0
    
    def __repr__(self):
        """
        Returns the customer order number when printing object
        """
        return self._customer_order_number
                
    def get_distributor(self):
        """
        Returns distributor data
        """
        return self._distributor

    def get_product_model(self):
        """
        Returns product model data
        """
        return self._product_model

    def get_order_date(self):
        """
        Returns order date data
        """
        return self._order_date

    def get_revenue(self):
        """
        Returns revenue date
        """
        return self._revenue

    def get_revenue_cost(self):
        """
        Returns revenue cost data
        """
        return self._revenue_cost
    
    def get_unit_revenue(self):
        """
        Returns booking unit data
        """
        return self._unit_revenue

    def get_net_profit_margin_revenue(self):
        """
        Returns net profit margin revenue
        """
        return self._net_profit_margin_revenue

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

def new_booking_data_non_currency_adjustment(each_order_number, extract_booking_list, not_currency_adjustment_booking_data_list):
    for current_booking_data in extract_booking_list:
        if current_booking_data.get_customer_order_number() == each_order_number:
            not_currency_adjustment_booking_data_list.append(Booking(current_booking_data.get_distributor(), current_booking_data.get_product_model(), each_order_number))
            return

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

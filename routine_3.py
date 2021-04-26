# Date: 28/03/2021
# Description: Automate routine task from work
#              Extract the booking and delivery info that is equal to 500k JPY or more than 500k JPY

import csv
import sys
from helper import *

class Booking:
    """
    Represents the booking data with data member such as 
    distributor, product model, order date,
    customer order number, cost, net sales, profit margin 
    and boolean to check if it is currency adjustment order,
    which default value is True.
    """

    def __init__(self, distributor, product_model, order_date, customer_order_number, booking, booking_cost):
        """
        Initialize data members for 
        distributor, product model, order date,
        customer order number, cost, net sales, profit margin 
        and boolean to check if it is currency adjustment order.
        """
        self._distributor = distributor
        self._product_model = product_model
        self._order_date = order_date
        self._customer_order_number = customer_order_number
        self._booking = booking
        self._booking_cost = booking_cost
        self._net_sales_booking = 0
        self._net_profit_margin_booking = 0
        self._is_currency_adjustment = True

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

    def get_net_sales_booking(self):
        """
        Returns net sales booking data
        """
        return self._net_sales_booking

    def get_net_profit_margin_booking(self):
        """
        Returns net profit margin booking
        """
        return self._net_profit_margin_booking

    def set_distributor(self, new_distributor):
        """
        Set distributor data to a new value
        """
        self._distributor = new_distributor

    def set_product_model(self, new_product_model):
        """
        Set product model data to a new value
        """
        self._product_model = new_product_model

    def set_order_date(self, new_order_date):
        """
        Set order date data to a new value
        """
        self._order_date = new_order_date

    def set_customer_order_number(self, new_customer_order_number):
        """
        Set customer order number data to a new value
        """
        self._customer_order_number = new_customer_order_number

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

    def set_net_sales_booking(self, new_net_sales_booking):
        """
        Set net sales booking data to a new value 
        """
        self._net_sales_booking = new_net_sales_booking

    def set_net_profit_margin_booking(self, new_net_profit_margin_booking):
        """
        Set net profit margin booking to a new value
        """
        self._net_profit_margin_booking = new_net_profit_margin_booking

    def set_currency_adjustment_boolean(self, boolean):
        """
        Update currency adjustment boolean
        """
        self._is_currency_adjustment = boolean

    def get_currency_adjustment_boolean(self):
        """
        Returns currency adjustment boolean data
        """
        return self._is_currency_adjustment

class Revenue:
    """
    Represents the revenue data with data member such as 
    distributor, product model, order date,
    customer order number, cost, net sales, profit margin.
    """

    def __init__(self, distributor, product_model, order_date, customer_order_number, revenue, revenue_cost):
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
        self._net_sales_revenue = 0
        self._net_profit_margin_revenue = 0
            
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

    def get_net_sales_revenue(self):
        """
        Returns net sales revenue data
        """
        return self._net_sales_revenue

    def get_net_profit_margin_revenue(self):
        """
        Returns net profit margin revenue
        """
        return self._net_profit_margin_revenue

    def set_distributor(self, new_distributor):
        """
        Set distributor data to a new value
        """
        self._distributor = new_distributor

    def set_product_model(self, new_product_model):
        """
        Set product model data to a new value
        """
        self._product_model = new_product_model

    def set_order_date(self, new_order_date):
        """
        Set order date data to a new value
        """
        self._order_date = new_order_date

    def set_customer_order_number(self, new_customer_order_number):
        """
        Set customer order number data to a new value
        """
        self._customer_order_number = new_customer_order_number

    def set_revenue(self, new_revenue):
        """
        Set revenue data to a new value
        """
        self._revenue = new_revenue

    def set_revenue_cost(self, new_revenue_cost):
        """
        Set revenue cost data to a new value 
        """
        self._revenue_cost = new_revenue_cost

    def set_net_sales_revenue(self, new_net_sales_revenue):
        """
        Set net sales revenue data to a new value 
        """
        self.net_sales_revenue = new_net_sales_revenue

    def set_net_profit_margin_revenue(self, new_net_profit_margin_revenue):
        """
        set net profit margin revenue to a new value
        """
        self.net_profit_margin_revenue = new_net_profit_margin_revenue


# Revenue
list_revenue_data = compute_revenue_list("cslrevenue.csv")

extract_revenue_list = []

for row in list_revenue_data:
    if int(row[12]) >= 500000: # Index 12th => Revenue
        extract_revenue_list.append(Revenue(row[0], row[9], row[15], row[24], row[12], row[13]))

for each_data in extract_revenue_list:

    net_sales = compute_net_sales(each_data) # Compute Net sales
    update_net_sales(each_data, net_sales) # Update Net sales

    net_profit_margin_non_percentage = compute_net_profit_margin(each_data) # Compute Net profit margin
    net_profit_margin = format_value_with_percentage(net_profit_margin_non_percentage) # Format value with percentage
    update_net_profit_margin(each_data, net_profit_margin) # Update Net profit margin

# for x in extract_revenue_list:
#     print(f"{int(x.get_revenue()):,}")
#     print(f"{int(x.get_revenue_cost()):,}")
#     print(f"{x.get_product_model()}")
#     print(f"{x.get_order_date()}")
#     print(f"{x.get_customer_order_number()}")
#     print(f"{int(x.get_net_sales_revenue()):,}")
#     print(f"{(x.get_net_profit_margin_revenue())}")

# Booking
list_booking_data = compute_booking_list("koreabooking.csv")

extract_booking_list = []

# >= 500,000
for row in list_booking_data:
    if int(row[12]) >= 500000: # Index 12th => Revenue
        extract_booking_list.append(Booking(row[0], row[9], row[15], row[24], row[12], row[13]))

for each_data in extract_booking_list:

    net_sales = compute_net_sales_booking(each_data) # Compute Net sales
    set_net_sales_booking(each_data, net_sales) # Update Net sales

    net_profit_margin_non_percentage = compute_net_profit_margin_booking(each_data) # Compute Net profit margin
    net_profit_margin = format_value_with_percentage(net_profit_margin_non_percentage) # Format value with percentage
    set_net_profit_margin_booking(each_data, net_profit_margin) # Update Net profit margin

# Create order number list
all_order_number_list = [each_order_number.get_customer_order_number() for each_order_number in extract_booking_list]
unique_order_number_set = set(all_order_number_list)
unique_order_number_list = list (unique_order_number_set)

# <= -500,000
for row in list_booking_data:
    if int(row[12]) <= -500000: # Index 12th => Revenue
        extract_booking_list.append(Booking(row[0], row[9], row[15], row[24], row[12], row[13]))   

# Extract non currency adjustment data
for each_order_number_list in unique_order_number_list:
    amount_list = [each_booking.get_booking() for each_booking in extract_booking_list if each_order_number_list == each_booking.get_customer_order_number()]
    # print(amount_list)
    total_amount = 0
    for each_amount in amount_list:
        total_amount += int(each_amount)
    print(total_amount)
    if total_amount > 0:
        for each_booking in extract_booking_list:
            if each_booking.get_customer_order_number() == each_order_number_list:
                each_booking.set_currency_adjustment_boolean(False)
    total_amount = 0 
    print(amount_list)   

for each_booking in extract_booking_list:
    if each_booking.get_currency_adjustment_boolean() == False:
        print(f"{int(each_booking.get_booking()):,}")
        print(f"{int(each_booking.get_booking_cost()):,}")
        print(f"{each_booking.get_product_model()}")
        print(f"{each_booking.get_order_date()}")
        print(f"{each_booking.get_customer_order_number()}")
        print(f"{int(each_booking.get_net_sales_booking()):,}")
        print(f"{(each_booking.get_net_profit_margin_booking())}")
        print(f"{(each_booking.get_currency_adjustment_boolean())}")
        print("\n")
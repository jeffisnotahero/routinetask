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
    and boolean to check if it is currency adjustment order.
    """

    def __init__(self, distributor, product_model, order_date, customer_order_number, booking, booking_cost, net_sales_booking, net_profit_margin_booking):
        """
        Initialize data members for 
        distributor, product model, order date,
        customer order number, cost, net sales, profit margin 
        and boolean to check if it is currency adjustment order.
        """
        self._distributor = distributor
        self._product_model = product_model
        self._order_date = order_date
        self._customer_order_number
        self._booking = booking
        self._booking_cost = booking_cost
        self._net_sales_booking = net_sales_booking
        self._net_profit_margin_booking = net_profit_margin_booking
        self._is_currency_adjustment = False

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
        return self.net_sales_booking

    def get_net_profit_margin_booking(self):
        """
        Returns net profit margin booking
        """
        return self.net_profit_margin_booking

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
        self.net_sales_booking = new_net_sales_booking

    def set_net_profit_margin_booking(self, new_net_profit_margin_booking):
        """
        Set net profit margin booking to a new value
        """
        self.net_profit_margin_booking = new_net_profit_margin_booking

    def set_net_profit_margin_booking(self, new_net_profit_margin_booking):
        """
        Set net profit margin booking to a new value
        """
        self.net_profit_margin_booking = new_net_profit_margin_booking

    def set_currency_adjustment_boolean(self, boolean):
        """
        Update currency adjustment boolean
        """
        self._is_currency_adjustment = boolean

class Revenue:
    """
    Represents the revenue data with data member such as 
    distributor, product model, order date,
    customer order number, cost, net sales, profit margin.
    """

    def __init__(self, distributor, product_model, order_date, customer_order_number, revenue, revenue_cost, net_sales_revenue, net_profit_margin_revenue):
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
        self._net_sales_revenue = net_sales_revenue
        self._net_profit_margin_revenue = net_profit_margin_revenue
            
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
        return self.net_sales_revenue

    def get_net_profit_margin_revenue(self):
        """
        Returns net profit margin revenue
        """
        return self.net_profit_margin_revenue

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
list_revenue_data = compute_revenue_list("korearevenue.csv")


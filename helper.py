import csv

class MonthlyPerformance:
    """
    Parent class for Monthly Performance
    """
    def __init__(self, name, booking=0, revenue=0, revenue_cost=0, net_sales_revenue=0, net_profit_margin_revenue=0, booking_cost=0, net_sales_booking=0, net_profit_margin_booking=0):
        self._name = name
        self._booking = booking
        self._revenue = revenue
        self._revenue_cost = revenue_cost
        self._net_sales_revenue = net_sales_revenue
        self._net_profit_margin_revenue = net_profit_margin_revenue
        self._booking_cost = booking_cost
        self._net_sales_booking = net_sales_booking
        self._net_profit_margin_booking = net_profit_margin_booking

    def __repr__(self):
        return self._name

    def print_info(self):

        print(f"""
        {self._name}\n
        Booking:            {self._booking:,} 
        Revenue:            {self._revenue:,} 
        Cost:               {self._revenue_cost:,} 
        Net sales:          {self._net_sales_revenue:,}
        Net profit margin:  {self._net_profit_margin_revenue}\n
        """, end='')
    
    def get_name(self):
        """
        Returns name data 
        """
        return self._name
    
    def get_revenue(self):
        """
        Returns revenue data
        """
        return self._revenue
    
    def get_cost(self):
        """
        Returns revenue cost data
        """
        return self._revenue_cost

    def get_net_sales_revenue(self):
        """
        Returns net sales for revenue
        """
        return self._net_sales_revenue

    def get_net_profit_margin_revenue(self):
        """
        Returns net profitmargin for revenue
        """
        return self._net_profit_margin_revenue

    def get_booking(self):
        """
        Returns booking data
        """
        return self._booking

    def get_booking_cost(self):
        """
        Returns booking cost
        """
        return self._booking_cost
    
    def get_net_sales_booking(self):
        """
        Returns net sales for booking
        """
        return self._net_sales_booking

    def get_net_profit_margin_booking(self):
        """
        Returns net profit margin for booking
        """
        return self._net_profit_margin_booking

class Distributor(MonthlyPerformance):
    """
    Distributor Child class that
    inherit Monthly Performance properties 
    """
    pass

class Region(MonthlyPerformance):
    """
    Region Child class that
    inherits Monthly Performance properties
    """
    pass

def compute_list(commandline_argument):
    """
    Returns a list of booking or revenue data opening booking data file with
    first parameter
    """
    # utf-8_sig
    # Open booking CSV and read everything into memory
    with open(commandline_argument, "r", encoding="shift_jis") as database:

        data = csv.reader(database)
        next(data)
        list_data = list(data)
        return list_data

def create_name_list(commandline_argument_1, commandline_argument_2):
    """
    Return a Distributor name list from Revenue csv file and Booking csv file,
    which both specified by 2 arguments
    """
    name_list = []

     # Populate name list
    list_revenue_data = compute_list(commandline_argument_1)
    for each_row in list_revenue_data:

        if each_row[0] not in name_list:
            name_list.append(each_row[0])

    # Populate name list
    list_booking_data = compute_list(commandline_argument_2)
    for each_row in list_booking_data:

        if each_row[0] not in name_list:
            name_list.append(each_row[0])

    return name_list

def update_revenue_and_cost(target_object, row):
    """
    Update the Distributor's revenue and cost data
    """
    revenue = row[12]
    target_object._revenue += int(revenue)
    cost = row[13]
    target_object._revenue_cost += int(cost)

def set_booking_cost(target_object, row):
    """
    Update the booking cost
    """
    cost = row[13] # Cost amount at 13th column
    target_object._booking_cost += int(cost)

def set_booking(target_object, row):
    """
    Update booking amount
    """
    booking = row[12] # Booking amount at 12th column
    target_object._booking += int(booking)


def compute_net_sales_booking(target_object):
    """
    Return net sales booking data by finding the difference
    of object's, which is an argument, revenue and cost data
    """
    net_sales_booking = int(target_object._booking) - int(target_object._booking_cost)
    return net_sales_booking

def set_net_sales_booking(target_object, net_sales_booking):
    """
    Update Distributor or Region's net sales booking data
    """
    target_object._net_sales_booking = net_sales_booking

def compute_net_profit_margin_booking(target_object):
    """
    Return net profit margin booking data by dividing the 
    object's, which is an argument, net sales data with
    revenue data.
    """

    # Check if division by zero (aka distributor.revenue == 0)
    if target_object._booking == 0:
        net_profit_margin_booking = 0
        return net_profit_margin_booking
    else:
        net_profit_margin_booking = int(target_object._net_sales_booking) / int(target_object._booking)
        return net_profit_margin_booking

def set_net_profit_margin_booking(target_object, profit_margin_booking):
    """
    Update Distributor or Region's profit margin booking data
    """
    target_object._net_profit_margin_booking = profit_margin_booking


def update_booking(target_object, row):
    """
    Update Distributor or Region's booking data
    """
    booking = row[12]
    target_object._booking += int(booking)






def update_net_sales(target_object, net_sales):
    """
    Update Distributor or Region's net sales data
    """
    target_object._net_sales_revenue = net_sales

def update_net_profit_margin(target_object, profit_margin):
    """
    Update Distributor or Region's profit margin data
    """
    target_object._net_profit_margin_revenue = profit_margin

def compute_net_sales(target_object):
    """
    Return net sales data by finding the difference
    of object's, which is an argument, revenue and cost data
    """
    net_sales = int(target_object._revenue) - int(target_object._revenue_cost)
    return net_sales

def compute_net_profit_margin(target_object):
    """
    Return net profit margin data by dividing the 
    object's, which is an argument, net sales data with
    revenue data.
    """
    # Check if division by zero (aka distributor.revenue == 0)
    if target_object._revenue == 0:
        net_profit_margin = 0
        return net_profit_margin
    else:
        net_profit_margin = int(target_object._net_sales_revenue) / int(target_object._revenue)
        return net_profit_margin


def format_value_with_percentage(original_value):
    """
    Return a value in percentage format from
    an input argument, the original value
    """
    percentage_value = "{0:.2%}".format(original_value)
    return percentage_value

class Deliverables:
    """
    Parent Class for Deliverables
    """
    def __init__(self, model, unit=0, estimated=0, normal_price =0, in_normal_price_list=True, in_discount_price_list=True):
        self.model = model
        self.unit = unit
        self.estimated = estimated
        self.normal_price = normal_price
        self.in_normal_price_list = in_normal_price_list
        self.in_discount_price_list = in_discount_price_list

    def __repr__(self):
        return self.model

    def print_info(self):

        print(f"""
        {self.model}\n
        Unit:                      {self.unit:,} 
        Estimated:                 {self.estimated:,} 
        Normal price:              {self.normal_price:,} 
        In normal price list:      {self.in_normal_price_list} 
        In discount price list:    {self.in_discount_price_list}\n
        """, end='')

def create_item_name_list(commandline_argument_1):
    """
    Return a product model name list from deliverables csv file,
    specified by an argument
    """
    item_name_list = []

    list_deliverables_data = compute_list(commandline_argument_1)

    # Populate name list
    for row in list_deliverables_data:
        same_name = False

        # Check if there is same name
        for items in list_deliverables_data:
            if items == row[1]:
                same_name = True
        
        # Insert into list if there is not
        if same_name == False:
            item_name_list.append(row[1])

    return item_name_list

def add_deliverables_unit_data(commandline_argument_1, product_list):
    """
    Add deliverables unit data into
    each deliverable from product list,
    which specified by second argument
    """
    with open(commandline_argument_1, "r", encoding="utf-8_sig") as deliverables_database:

            deliverables_data = csv.reader(deliverables_database)
            next(deliverables_data)
            list_deliverables_data = list(deliverables_data)

            length_product_list = len(product_list)
            for model in range(length_product_list):
                product_list[model].unit += int(list_deliverables_data[model][2]) # [2] product unit

def add_discount_price(commandline_argument_2, product_list):
    """
    Add all available discount price for
    deliverables and set in_discount_price_list to True,
    if there is none
    """
    with open(commandline_argument_2, "r", encoding="utf-8_sig") as discount_price_list_database:

        discount_price_list_data = csv.reader(discount_price_list_database)
        next(discount_price_list_data)
        discount_price_list = list(discount_price_list_data)

    # Label discount price
    for product in product_list:

        product.in_discount_price_list = False

        # Loop all price list to find if curreunt model has a discount price
        for product_from_discount_list in discount_price_list:

            if product.model == product_from_discount_list[6]: # [6] => 
                product.estimated = product.unit * float(product_from_discount_list[7]) # [7] => price column
                product.in_discount_price_list = True
                break

def add_normal_price(commandline_argument, product_list):
    """
    Add all available normal price for
    deliverables and set in_discount_price_list to True,
    if there is none
    """
    with open(commandline_argument, "r", encoding="utf-8_sig") as normal_price_list_database:
        normal_price_list_data = csv.reader(normal_price_list_database)
        next(normal_price_list_data)
        normal_price_list = list(normal_price_list_data)

    # Labal normal price
    for product in product_list:

        product.in_normal_price_list = False

        for product_from_normal_list in normal_price_list:
            
            if product.model == product_from_normal_list[1]:
                product.normal_price = product.unit * float(product_from_normal_list[2]) # [2] => price column
                product.in_normal_price_list = True
                break

def compute_revenue_data(commandline_argument, region_monthly_performance):
    """
    Compute revenue data with revenue csv file specified by first argument,
    and add the data into Region Monthly Performance object
    """
    list_revenue_data = compute_list(commandline_argument)

    # Compute Region Monthly Total Booking
    for row in list_revenue_data:

        update_revenue_and_cost(region_monthly_performance, row)
    
    region_net_sales = compute_net_sales(region_monthly_performance) # Compute Region's Net sales
    update_net_sales(region_monthly_performance, region_net_sales) # Update Region's Net sales

    region_net_profit_margin_non_percentage = compute_net_profit_margin(region_monthly_performance) # Compute Region's Net profit margin
    region_net_profit_margin = format_value_with_percentage(region_net_profit_margin_non_percentage) # Format value with percentage
    update_net_profit_margin(region_monthly_performance, region_net_profit_margin) # Update Region's Net profit margin

def currency_conversion(price_amount, conversion_rate):
    """
    Returns price amount converted
    with converstion rate specified
    by second argument.
    """
    return price_amount * 109

def check_all_deliverables_with_required_price(product_list, in_discount_or_normal_price_list):
    """
    Return a counter showing if there is missing
    discount or normal price for either each deliverables
    supposed to have discount or normal price respectively,
    which specified by second argument
    """
    is_discount_or_normal_price_list_counter = 0
    for product in product_list:
        
        if getattr(product, in_discount_or_normal_price_list) == False:
            is_discount_or_normal_price_list_counter += 1

    return is_discount_or_normal_price_list_counter

def compute_total_deliverables_if_all_with_required_price(product_list, discount_or_normal_price, region_monthly_performance):
    """
    Print the current and total expected deliverables,
    after computation of total deliverables if only
    all deliverables from product list have either price
    supposed to have, normal or discount, which specified by
    second argument for checking it.
    """
    current_deliverables = 0

    for product in product_list:
        current_deliverables += getattr(product, discount_or_normal_price)

    jpy_current_deliverables = currency_conversion(current_deliverables, 109) # Convert to JPY currency
    total_deliverables = jpy_current_deliverables + region_monthly_performance.revenue
    
    print_current_and_total_expected_deliverables(jpy_current_deliverables, total_deliverables)

def prompt_user_plug_in_estimated_normal_price(product_list):
    """
    Prompt user to plug in their estimated normal price,
    if only the deliverable from product list does not have one
    """
    # Show user the items that without the normal price
    for product in product_list:

        if product.in_normal_price_list == False:
            product.print_info()
    
    # Prompt user for normal price input for those product
    for product in product_list:

        if product.in_normal_price_list == False:
            print("\n")
            print(f"Plug in estimated normal price for, {product.model}:")
            estimated_normal_price = float(input())
            product.normal_price = estimated_normal_price * product.unit

def prompt_user_plug_in_estimated_discount_price(product_list):
    """
    Prompt user to plug in their estimated discount price,
    if only the deliverable from product list does not have one
    """
    for product in product_list:

        if product.in_discount_price_list == False:
            product.print_info()
    
    # Prompt user for normal price input for those product
    for product in product_list:

        if product.in_discount_price_list == False:
            print("Plug in estimated discount price for", product.model)
            estimated_discount_price = float(input("estimated discount price: \n"))
            product.estimated = estimated_discount_price * product.unit

def check_total_numbers_unavailable_normal_or_discount_price(product_list, discount_or_normal_price):
    """
    Print out the total numbers of deliverable that
    does not have price supposed to have, discount or normal price,
    which specified by second argument.
    """
    product_not_in_normal_or_discount_price_list_counter = 0

    for product in product_list:

        if getattr(product, discount_or_normal_price) == False:
            product_not_in_normal_or_discount_price_list_counter += 1
    
    product_list_length = len(product_list)

    print("\n")
    print(product_not_in_normal_or_discount_price_list_counter, "out of", product_list_length, "is not", discount_or_normal_price)


def print_current_and_total_expected_deliverables(current_deliverables, total_deliverables):
    """
    Print out the current deliverables and,
    total expected deliverables
    """
    print(f"\n")
    print(f"deliverables: {current_deliverables:,.2f}")
    print(f"total_expected_deliverables: {total_deliverables:,.2f}")
    print(f"\n")
    
def compute_final_data_based_on_input_selection(product_list, in_normal_or_discount_price_list, normal_or_discount_price, region_monthly_performance):
    """
    Print out the current deliverables and,
    total expected deliverables based on the 
    user decision, whereby either compute the final data,
    with estimated discount or normal price, based on computation
    of data and specified with second argument.
    """
    
    user_decision = int(input())

    current_deliverables = 0

    if user_decision == 1:
        

        for product in product_list:

            if getattr(product, in_normal_or_discount_price_list) == True or getattr(product, in_normal_or_discount_price_list) == False:
                current_deliverables += getattr(product, normal_or_discount_price)

        jpy_current_deliverables = currency_conversion(current_deliverables, 109) # Convert to JPY currency
        total_deliverables = jpy_current_deliverables + region_monthly_performance._revenue

        for product in product_list:
            if getattr(product, in_normal_or_discount_price_list) == False:
                product.print_info()

        print_current_and_total_expected_deliverables(jpy_current_deliverables, total_deliverables)

    else:

        for product in product_list:

            if getattr(product, in_normal_or_discount_price_list) == True:
                current_deliverables += getattr(product, normal_or_discount_price)

        jpy_current_deliverables = currency_conversion(current_deliverables, 109) # Convert to JPY currency
        total_deliverables = jpy_current_deliverables + region_monthly_performance._revenue

        for product in product_list:
            if getattr(product, in_normal_or_discount_price_list)  == False:
                product.print_info()

        print_current_and_total_expected_deliverables(jpy_current_deliverables, total_deliverables)


# Helper functions for routine_3.py
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

def new_booking_data_non_currency_adjustment(each_order_number, extract_booking_list, not_currency_adjustment_booking_data_list):
    """
    Function that takes order number from not_currency_adjustment_order_number_list. extract_booking_list as input,
    and add Booking object, with the distributor, product model and order number of booking data from extract_booking_list,
    if input order number is same as customer order number of each booking data from extract_booking_list, eventually return nothing.
    """
    for current_booking_data in extract_booking_list:
        if current_booking_data.get_customer_order_number() == each_order_number:
            not_currency_adjustment_booking_data_list.append(Booking(current_booking_data.get_distributor(), current_booking_data.get_product_model(), each_order_number))
            return
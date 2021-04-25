import csv

class MonthlyPerformance:
    """
    Parent class for Monthly Performance
    """
    def __init__(self, name, booking=0, revenue=0, cost=0, net_sales=0, net_profit_margin=0, booking_cost=0, net_sales_booking=0, net_profit_margin_booking=0):
        self.name = name
        self.booking = booking
        self.revenue = revenue
        self.cost = cost
        self.net_sales = net_sales
        self.net_profit_margin = net_profit_margin
        self._booking_cost = booking_cost
        self._net_sales_booking = net_sales_booking
        self._net_profit_margin_booking = net_profit_margin_booking

    def __repr__(self):
        return self.name

    def print_info(self):

        print(f"""
        {self.name}\n
        Booking:            {self.booking:,} 
        Revenue:            {self.revenue:,} 
        Cost:               {self.cost:,} 
        Net sales:          {self.net_sales:,}
        Net profit margin:  {self.net_profit_margin}\n
        """, end='')
    
    def get_revenue(self):
        """
        Returns revenue data
        """
        return self.revenue
    
    def get_cost(self):
        """
        Returns revenue cost data
        """
        return self.cost

    def get_net_sales_revenue(self):
        """
        Returns net sales for revenue
        """
        return self.net_sales

    def get_net_profit_margin_revenue(self):
        """
        Returns net profitmargin for revenue
        """
        return self.net_profit_margin

    def get_booking(self):
        """
        Returns booking data
        """
        return self.booking

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

def create_name_list(commandline_argument_1, commandline_argument_2):
    """
    Return a Distributor name list from Revenue csv file and Booking csv file,
    which both specified by 2 arguments
    """
    name_list = []

    # Add name from both csv
    with open(commandline_argument_1, "r", encoding="shift_jis") as revenue_database, open(commandline_argument_2, "r", encoding="shift_jis") as booking_database:

        revenue_data = csv.reader(revenue_database)
        next(revenue_data)
        list_revenue_data = list(revenue_data)

        # Populate name list
        for row in list_revenue_data:
            same_name = False

            # Check if there is same name
            for items in name_list:
                if items == row[0]:
                    same_name = True
            
            # Insert into list if there is not
            if same_name == False:
                name_list.append(row[0])

        booking_data = csv.reader(booking_database)
        next(booking_data)
        list_booking_data = list(booking_data)

        # Populate name list
        for row in list_booking_data:
            same_name = False

            # Check if there is same name
            for items in name_list:
                if items == row[0]:
                    same_name = True
            
            # Insert into list if there is not
            if same_name == False:
                name_list.append(row[0])

    return name_list

def update_revenue_and_cost(target_object, row):
    """
    Update the Distributor's revenue and cost data
    """
    revenue = row[12]
    target_object.revenue += int(revenue)
    cost = row[13]
    target_object.cost += int(cost)

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
    target_object.booking += int(booking)

def compute_net_sales_booking(target_object):
    """
    Return net sales booking data by finding the difference
    of object's, which is an argument, revenue and cost data
    """
    net_sales_booking = target_object.booking - target_object._booking_cost
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
    if target_object.booking == 0:
        net_profit_margin_booking = 0
        return net_profit_margin_booking
    else:
        net_profit_margin_booking = target_object._net_sales_booking / target_object.booking
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
    target_object.booking += int(booking)

def update_net_sales(target_object, net_sales):
    """
    Update Distributor or Region's net sales data
    """
    target_object.net_sales = net_sales

def update_net_profit_margin(target_object, profit_margin):
    """
    Update Distributor or Region's profit margin data
    """
    target_object.net_profit_margin = profit_margin

def compute_net_sales(target_object):
    """
    Return net sales data by finding the difference
    of object's, which is an argument, revenue and cost data
    """
    net_sales = target_object.revenue - target_object.cost
    return net_sales

def compute_net_profit_margin(target_object):
    """
    Return net profit margin data by dividing the 
    object's, which is an argument, net sales data with
    revenue data.
    """

    # Check if division by zero (aka distributor.revenue == 0)
    if target_object.revenue == 0:
        net_profit_margin = 0
        return net_profit_margin
    else:
        net_profit_margin = target_object.net_sales / target_object.revenue
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

    # Add name from both csv
    with open(commandline_argument_1, "r") as deliverables_database:

        deliverables_data = csv.reader(deliverables_database)
        next(deliverables_data)
        list_deliverables_data = list(deliverables_data)

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

def compute_booking_list(commandline_argument):
    """
    Returns a list of booking data opening booking data file with
    first parameter
    """
    # Open booking CSV and read everything into memory
    with open(commandline_argument, "r", encoding="shift_jis") as database:

        # row[0] : "distributor"
        # row[12] : "booking"
        # row[13] : "cost"
        booking_data = csv.reader(database)
        next(booking_data)
        list_booking_data = list(booking_data)
        return list_booking_data

def compute_revenue_list(commandline_argument):
        """
        Returns a list of revenue data opening revenue data file with
        first parameter
        """
        # Open revenue CSV and read everything into memory
        with open(commandline_argument, "r", encoding="shift_jis") as database:

            # row[0] : "distributor"
            # row[12] : "revenue"
            # row[13] : "cost"
            revenue_data = csv.reader(database)

            next(revenue_data) # Skip first row (Description row)
            list_revenue_data = list(revenue_data) # Convert csv data to list 
            return list_revenue_data

def compute_revenue_data(commandline_argument, region_monthly_performance):
    """
    Compute revenue data with revenue csv file specified by first argument,
    and add the data into Region Monthly Performance object
    """
    list_revenue_data = compute_revenue_list(commandline_argument)

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
        total_deliverables = jpy_current_deliverables + region_monthly_performance.revenue

        for product in product_list:
            if getattr(product, in_normal_or_discount_price_list) == False:
                product.print_info()

        print_current_and_total_expected_deliverables(jpy_current_deliverables, total_deliverables)

    else:

        for product in product_list:

            if getattr(product, in_normal_or_discount_price_list) == True:
                current_deliverables += getattr(product, normal_or_discount_price)

        jpy_current_deliverables = currency_conversion(current_deliverables, 109) # Convert to JPY currency
        total_deliverables = jpy_current_deliverables + region_monthly_performance.revenue

        for product in product_list:
            if getattr(product, in_normal_or_discount_price_list)  == False:
                product.print_info()

        print_current_and_total_expected_deliverables(jpy_current_deliverables, total_deliverables)



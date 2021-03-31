import csv

# Parent Class
class MonthlyPerformance:
    def __init__(self, name, booking=0, revenue=0, cost=0, net_sales=0, net_profit_margin=0):
        self.name = name
        self.booking = booking
        self.revenue = revenue
        self.cost = cost
        self.net_sales = net_sales
        self.net_profit_margin = net_profit_margin

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

# Create Child class (Distributor)
class Distributor(MonthlyPerformance):
    pass

# Create Child class (Region)
class Region(MonthlyPerformance):
    pass

# Function for creating name list
def create_name_list(commandline_argument_1, commandline_argument_2):

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

# Function for updating Revenue & Cost
def update_revenue_and_cost(target_object, row):
    revenue = row[12]
    target_object.revenue += int(revenue)
    cost = row[13]
    target_object.cost += int(cost)

# Function for updating Booking
def update_booking(target_object, row):
    booking = row[12]
    target_object.booking += int(booking)

# Function for updating Net sales
def update_net_sales(target_object, net_sales):
    target_object.net_sales = net_sales

# Function for updating Net profit margin
def update_net_profit_margin(target_object, profit_margin):
    target_object.net_profit_margin = profit_margin

# Function for computing Net sales
def compute_net_sales(target_object):
    net_sales = target_object.revenue - target_object.cost
    return net_sales

# Function for computing Net profit margin
def compute_net_profit_margin(target_object):

    # Check if division by zero (aka distributor.revenue == 0)
    if target_object.revenue == 0:
        net_profit_margin = 0
        return net_profit_margin
    else:
        net_profit_margin = target_object.net_sales / target_object.revenue
        return net_profit_margin

# Format valye with percentage
def format_value_with_percentage(original_value):
    percentage_value = "{0:.2%}".format(original_value)
    return percentage_value
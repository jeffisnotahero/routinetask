# Parent Class
class MonthlyPerformance:
    def __init__(self, name, booking, revenue, cost, net_sales, net_profit_margin):
        self.name = name
        self.booking = booking
        self.revenue = revenue
        self.cost = cost
        self.net_sales = net_sales
        self.net_profit_margin = net_profit_margin

    def __repr__(self):
        return self.name

# Create Child class (Distributor)
class Distributor(MonthlyPerformance):
    pass


# Create Child class (Region)
class Region(MonthlyPerformance):
    pass

# Function for updating distributors' Revenue & Cost
def update_revenue_and_cost(target_object, row):
    revenue = row[12]
    target_object.revenue += int(revenue)
    cost = row[13]
    target_object.cost += int(cost)

# Function for updating distributors' Net sales
def update_net_sales(target_object, net_sales):
    target_object.net_sales = net_sales

# Function for updating distributor's Net profit margin
def update_net_profit_margin(target_object, profit_margin):
    target_object.net_profit_margin = profit_margin

# Function for computing distributors' Net sales
def compute_net_sales(target_object):
    net_sales = target_object.revenue - target_object.cost
    return net_sales

# Function for computing distributors' Net profit margin
def compute_net_profit_margin(target_object):

    # Check if division by zero (aka distributor.revenue == 0)
    if target_object.revenue == 0:
        net_profit_margin = 0
        return net_profit_margin
    else:
        net_profit_margin = target_object.net_sales / target_object.revenue
        return net_profit_margin

def format_value_with_percentage(original_value):
    percentage_value = "{0:.2%}".format(original_value)
    return percentage_value
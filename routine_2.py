# Date: 28/03/2021
# Description: Automate routine task from work
#              Compute forecasted revenue & booking performance(few days before next month) and display the output

import csv
import sys
from helper import *

# # Check command-line argument
# if len(sys.argv) != 4:
#     print("Usage: python routine.py 'YOUR DELIVERABLE CSV'.csv 'YOUR DISCOUNT PRICE LIST CSV'.csv 'YOUR NORMAL PRICE LIST CSV'.csv ----MUST FOLLOW THE ORDER OF INPUT OF CSV FILE!!!----")
#     sys.exit(1)

# Parent Class Deliverables
class Deliverables:
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

# Function for creating name list
def create_item_name_list(commandline_argument_1):

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

# Create item list
item_name_list = create_item_name_list("koreadelivery.csv")
# print(item_name_list)

# Create item object and insert into list
item_list = []
for name in item_name_list:
    item_list.append(Deliverables(name))

# for item in item_list:
#     print(item.model)

# Add units
with open("koreadelivery.csv", "r") as deliverables_database:

        deliverables_data = csv.reader(deliverables_database)
        next(deliverables_data)
        list_deliverables_data = list(deliverables_data)

        length_item_list = len(item_list)
        for i in range(length_item_list):
            item_list[i].unit += int(list_deliverables_data[i][2])

# for i in range(length_item_list):
#             print(item_list[i].model, item_list[i].unit)
        
            
#check every item could be priced with discount list and normal list and label it
with open("specialpricelist.csv", "r") as discount_price_list_database, open("normalpricelist.csv", "r") as normal_price_list_database:

    discount_price_list_data = csv.reader(discount_price_list_database)
    next(discount_price_list_data)
    discount_price_list = list(discount_price_list_data)
    
    normal_price_list_data = csv.reader(normal_price_list_database)
    next(normal_price_list_data)
    normal_price_list = list(normal_price_list_data)

    # for product_from_discount_list in discount_price_list:
    #     print(product_from_discount_list[7])
  
    # label discount price
    for product in item_list:

        in_discount_price_list = False

        # loop all price list to find if current model has a discount price
        for product_from_discount_list in discount_price_list:

            if product.model == product_from_discount_list[6]:
                product.estimated = product.unit * float(product_from_discount_list[7]) # [7] => price column
                in_discount_price_list = True
                break
        
        # If current product has no discount price after all checks then label it
        if in_discount_price_list == False:

                product.in_discount_price_list = False
        
        # Reset boolean
        in_discount_price_list = False
    
    # labal normal price
    for product in item_list:

        in_normal_price_list = False

        for product_from_normal_list in normal_price_list:
            
            if product.model == product_from_normal_list[1]:
                product.normal_price = float(product_from_normal_list[2]) # [2] => price column
                in_normal_price_list = True
                break

        if in_normal_price_list == False:
                product.in_normal_price_list = False
        
        in_normal_price_list = False

        # for product_from_normal_list in normal_price_list:
        #     print (product_from_normal_list[2],product_from_normal_list[1])

# // action taken in prior for what if there is items cannot be priced in normal price list

# # Show user the items that without the normal price
# for product in item_list:

#     if product.in_normal_price_list == False:
#         product.print_info()

# user_input = input("Plug in normal price? y for go, n for nah\n")

# if user_input == "y":

#     # Prompt user for normal price input for those product
#     for product in item_list:

#         if product.in_normal_price_list == False:
#             print("Plug in normal price for", product.model, "?")
#             estimated_normal_price = float(input("normal price:"))
#             product.normal_price = estimated_normal_price

# Region monthly performance object
region_monthly_performance = Region("Region_monthly_performance")

# Open revenue CSV and read everything into memory
# with open("revenue.csv", "r", encoding="shift_jis") as database:

#     # row[0] : "distributor"
#     # row[12] : "revenue"
#     # row[13] : "cost"
#     revenue_data = csv.reader(database)

#     next(revenue_data) # Skip first row (Description row)
#     list_revenue_data = list(revenue_data) # Convert csv data to list 

#     # Compute Region Monthly Total Booking
#     for row in list_revenue_data:

#         update_revenue_and_cost(region_monthly_performance, row)
    
#     region_net_sales = compute_net_sales(region_monthly_performance) # Compute Region's Net sales
#     update_net_sales(region_monthly_performance, region_net_sales) # Update Region's Net sales

#     region_net_profit_margin_non_percentage = compute_net_profit_margin(region_monthly_performance) # Compute Region's Net profit margin
#     region_net_profit_margin = format_value_with_percentage(region_net_profit_margin_non_percentage) # Format value with percentage
#     update_net_profit_margin(region_monthly_performance, region_net_profit_margin) # Update Region's Net profit margin

# region_monthly_performance.print_info()





# // prompt decision before compute final data
# -loop item list

#     -if there is item.booleam.check_if_in_discount_price_false
#         -print how many are there and those info
#         -prompt user if they want compute those with normal price or not and show output
#             -if true
#                 -loop normal price and compute estimated & cost and update those item estimated & cost

#                 -loop items list, sum total revenue and delivery amount, compute net profit margin and show output
#             -else
#                 -loop item list, sum delivery amount (item boolean check = true), compute net profit margin and show output
#                 -print those item that not existed in the discount list
    
#     -else
#         -loop item list, sum every delivery amount (item boolean check = true), compute net profit margin and show output
#         -print those item
#         -print all items in discount list




# for item in item_list:
#     item.print_info
# for i in range(length_item_list):
#             print(item_list[i].model, item_list[i].unit, item_list[i].estimated, item_list[i].in_discount_price_list, item_list[i].normal_price, item_list[i].in_normal_price_list)

# for product in item_list:
#     product.print_info()

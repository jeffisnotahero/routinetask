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
        In normal price list:      {self.in_normal_price_list:,} 
        In discount price list:    {self.in_discount_price_list:,}
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
        # print(list_deliverables_data)

        length_item_list = len(item_list)
        for i in range(length_item_list):
            item_list[i].unit += int(list_deliverables_data[i][2])

for i in range(length_item_list):
            print(item_list[i].model, item_list[i].unit)
        
            
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
  

    for product in item_list:

        success = 0

        for product_from_discount_list in discount_price_list:

            if product.model == product_from_discount_list[6]:
                product.estimated = product.unit * float(product_from_discount_list[7]) # [7]Price
                success += 1
                break

        if success == 0:

                product.in_discount_price_list = False
        
        success = 0
                
    for product in item_list:

        success1 = 0

        for product_from_normal_list in normal_price_list:
            
            if product.model == product_from_normal_list[1]:
                product.normal_price = product_from_normal_list[2]
                success1 += 1
                break

        if success1 == 0:
                product.in_normal_price_list = False
        
        success1 = 0

        # for product_from_normal_list in normal_price_list:
        #     print (product_from_normal_list[2],product_from_normal_list[1])

# for item in item_list:
#     item.print_info
for i in range(length_item_list):
            print(item_list[i].model, item_list[i].unit, item_list[i].estimated, item_list[i].in_discount_price_list, item_list[i].normal_price, item_list[i].in_normal_price_list)
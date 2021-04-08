# Date: 28/03/2021
# Description: Automate routine task from work
#              Compute forecasted revenue & booking performance(few days before next month) and display the output

import csv
import sys
from helper import *

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

# Check command-line argument 
if len(sys.argv) > 5 or len(sys.argv) < 4:
    print(f"""
                                            ----MUST FOLLOW THE ORDER OF INPUT OF CSV FILE!!!---- 
        Usage: python routine.py 'DELIVERABLES'.csv, 'DSICOUNT PRICE LIST'.csv, 'NORMAL PRICE LIST'.csv, 'REVENUE AS OF NOW'.csv for Korea data;
        Usage: python routine.py 'DELIVERABLES'.csv, 'NORMAL PRICE LIST'.csv, 'REVENUE AS OF NOW'.csv for China data
                                            ----MUST FOLLOW THE ORDER OF INPUT OF CSV FILE!!!---- 
        \n""")
    sys.exit(1)

# Prompt user which data to be computed
incoming_computed_data = int(input("Enter 1 if Korea data, Enter 2 if China data \n"))
if incoming_computed_data == 1:

    # Create item list
    item_name_list = create_item_name_list(sys.argv[1])
    # print(item_name_list)

    # Create item object and insert into list
    item_list = []
    for name in item_name_list:
        item_list.append(Deliverables(name))

    # Add units
    with open(sys.argv[1], "r") as deliverables_database:

            deliverables_data = csv.reader(deliverables_database)
            next(deliverables_data)
            list_deliverables_data = list(deliverables_data)

            length_item_list = len(item_list)
            for i in range(length_item_list):
                item_list[i].unit += int(list_deliverables_data[i][2])

                
    #check every item could be priced with discount list and normal list and label it
    with open(sys.argv[2], "r") as discount_price_list_database, open(sys.argv[3], "r") as normal_price_list_database:

        discount_price_list_data = csv.reader(discount_price_list_database)
        next(discount_price_list_data)
        discount_price_list = list(discount_price_list_data)
        
        normal_price_list_data = csv.reader(normal_price_list_database)
        next(normal_price_list_data)
        normal_price_list = list(normal_price_list_data)

        # Label discount price
        for product in item_list:

            product.in_discount_price_list = False

            # loop all price list to find if curreunt model has a discount price
            for product_from_discount_list in discount_price_list:

                if product.model == product_from_discount_list[6]:
                    product.estimated = product.unit * float(product_from_discount_list[7]) # [7] => price column
                    product.in_discount_price_list = True
                    break

        # labal normal price
        for product in item_list:

            product.in_normal_price_list = False

            for product_from_normal_list in normal_price_list:
                
                if product.model == product_from_normal_list[1]:
                    product.normal_price = float(product_from_normal_list[2]) # [2] => price column
                    product.in_normal_price_list = True
                    break


    # ompute total revenue & cost as of now
    # Region monthly performance object
    region_monthly_performance = Region("Region_monthly_performance")

    # Open revenue CSV and read everything into memory
    with open(sys.argv[4], "r", encoding="shift_jis") as database:

        # row[0] : "distributor"
        # row[12] : "revenue"
        # row[13] : "cost"
        revenue_data = csv.reader(database)

        next(revenue_data) # Skip first row (Description row)
        list_revenue_data = list(revenue_data) # Convert csv data to list 

        # Compute Region Monthly Total Booking
        for row in list_revenue_data:

            update_revenue_and_cost(region_monthly_performance, row)
        
        region_net_sales = compute_net_sales(region_monthly_performance) # Compute Region's Net sales
        update_net_sales(region_monthly_performance, region_net_sales) # Update Region's Net sales

        region_net_profit_margin_non_percentage = compute_net_profit_margin(region_monthly_performance) # Compute Region's Net profit margin
        region_net_profit_margin = format_value_with_percentage(region_net_profit_margin_non_percentage) # Format value with percentage
        update_net_profit_margin(region_monthly_performance, region_net_profit_margin) # Update Region's Net profit margin

    region_monthly_performance.print_info()

    # if everything has discount price compute immediately
    is_discount_price_list_counter = 0

    for product in item_list:
        
        if product.in_discount_price_list == False:
            is_discount_price_list_counter += 1

    if is_discount_price_list_counter == 0:
        

        current_deliverables = 0
        for product in item_list:
            current_deliverables += product.estimated
            product.print_info()

        # Multiply 109 for conversion from USD TO JPY
        total_deliverables = (current_deliverables * 109) + region_monthly_performance.revenue
        
        print(f"\n")
        print(f"deliverables: {current_deliverables:,}")
        print(f"total_expected_deliverables: {total_deliverables:,}")
        print(f"\n")

    # else handling
    else:
        # Check and plug in estiamted normal price for those products without 
        # Show user the items that without the normal price
        for product in item_list:

            if product.in_normal_price_list == False:
                product.print_info()
        
        # Prompt user for normal price input for those product
        for product in item_list:

            if product.in_normal_price_list == False:
                print("Plug in estimated normal price for", product.model)
                estimated_normal_price = float(input("estiamted normal price: \n"))
                product.normal_price = estimated_normal_price * product.unit
        

        # Check and plug in estiamted discount price for those products without 
        for product in item_list:

            if product.in_discount_price_list == False:
                product.print_info()
        
        # Prompt user for normal price input for those product
        for product in item_list:

            if product.in_discount_price_list == False:
                print("Plug in estimated discount price for", product.model)
                estimated_discount_price = float(input("estimated discount price: \n"))
                product.estimated = estimated_discount_price * product.unit


        # prompt decision before compute final data
        # Show user how many are item without normal and discount as well as item without discount only
        in_discount_and_normal_price_list_counter = 0
        in_only_discount_price_list_counter = 0
        in_only_normal_price_list_counter = 0

        for product in item_list:
            if product.in_discount_price_list == True and product.in_normal_price_list == True:
                in_discount_and_normal_price_list_counter += 1
                
            elif product.in_discount_price_list == True and product.in_normal_price_list == False:
                in_only_discount_price_list_counter += 1

            elif product.in_discount_price_list == False and product.in_normal_price_list == True:
                in_only_normal_price_list_counter += 1

        item_list_length = len(item_list)
        
        print(in_discount_and_normal_price_list_counter, "out of", item_list_length, "does have both prices")
        print(in_only_discount_price_list_counter, "out of", item_list_length, "have discount price only")
        print(in_only_normal_price_list_counter, "out of", item_list_lenght, "have normal price only")

        print(f"""
        Enter 
        1: Compute final data with newly estimated normal price, 
        2: Compute final data with only available normal price """)

        user_decision = int(input())


        if user_decision == 1:
            
            current_deliverables = 0

            for product in item_list:

                if product.in_discount_price_list == True:
                    current_deliverables += product.estimated
                else:
                    current_deliverables += product.normal_price

            total_deliverables = (current_deliverables * 109) + region_monthly_performance.revenue

            for item in item_list:
                if item.in_discount_price_list == False:
                    item.print_info()
            
            print(f"\n")
            print(f"deliverables: {current_deliverables:,}")
            print(f"total_expected_deliverables: {total_deliverables:,}")
            print(f"\n")
        
        else:
            current_deliverables = 0

            for product in item_list:

                if product.in_discount_price_list == True:
                    current_deliverables += product.estimated

            total_deliverables = (current_deliverables * 109) + region_monthly_performance.revenue

            for item in item_list:
                if item.in_discount_price_list == False:
                    item.print_info()
            
            print(f"\n")
            print(f"deliverables: {current_deliverables:,}")
            print(f"total_expected_deliverables: {total_deliverables:,}")
            print(f"\n")

# Handle China data
else:
    # Create item list
    item_name_list = create_item_name_list("csldeliverable.csv")

    # Create item object and insert into list
    item_list = []
    for name in item_name_list:
        item_list.append(Deliverables(name, in_discount_price_list=False))

    # Add units
    with open("csldeliverable.csv", "r") as deliverables_database:

            deliverables_data = csv.reader(deliverables_database)
            next(deliverables_data)
            list_deliverables_data = list(deliverables_data)

            length_item_list = len(item_list)
            for i in range(length_item_list):
                item_list[i].unit += int(list_deliverables_data[i][2])

                
    #check every item could be priced with discount list and normal list and label it
    with open("cslnormalpricelist.csv", "r") as normal_price_list_database:
        
        normal_price_list_data = csv.reader(normal_price_list_database)
        next(normal_price_list_data)
        normal_price_list = list(normal_price_list_data)

        # label normal price
        for product in item_list:

            # Assume all producs are not in normal price list
            product.in_normal_price_list = False

            # loop all price list to find if curreunt model has a normal price
            for product_from_normal_list in normal_price_list:

                if product.model == product_from_normal_list[1]:    # [1] => model column
                    product.estimated = product.unit * float(product_from_normal_list[2]) # [2] => price column
                    product.in_normal_price_list = True
                    break

    # Compute total revenue & cost as of now

    # Region monthly performance object
    region_monthly_performance = Region("Region_monthly_performance")

    # Open revenue CSV and read everything into memory
    with open("cslrevenue.csv", "r", encoding="shift_jis") as database:

        # row[0] : "distributor"
        # row[12] : "revenue"
        # row[13] : "cost"
        revenue_data = csv.reader(database)

        next(revenue_data) # Skip first row (Description row)
        list_revenue_data = list(revenue_data) # Convert csv data to list 

        # Compute Region Monthly Total Booking
        for row in list_revenue_data:

            update_revenue_and_cost(region_monthly_performance, row)
        
        region_net_sales = compute_net_sales(region_monthly_performance) # Compute Region's Net sales
        update_net_sales(region_monthly_performance, region_net_sales) # Update Region's Net sales

        region_net_profit_margin_non_percentage = compute_net_profit_margin(region_monthly_performance) # Compute Region's Net profit margin
        region_net_profit_margin = format_value_with_percentage(region_net_profit_margin_non_percentage) # Format value with percentage
        update_net_profit_margin(region_monthly_performance, region_net_profit_margin) # Update Region's Net profit margin

    region_monthly_performance.print_info()

    # if everything has normal price compute immediately
    is_normal_price_list_counter = 0

    for product in item_list:
        
        if product.in_normal_price_list == False:
            is_normal_price_list_counter += 1

    if is_normal_price_list_counter == 0:
        
        current_deliverables = 0
        for product in item_list:
            current_deliverables += product.estimated
        
        total_deliverables = (current_deliverables * 109) + region_monthly_performance.revenue

        print(f"\n")
        print(f"deliverables: {current_deliverables:,}")
        print(f"total_expected_deliverables: {total_deliverables:,}")
        print(f"\n")

    # else handling
    else:
        # Check and plug in estiamted normal price for those products without 
        # Show user the items that without the normal price
        for product in item_list:

            if product.in_normal_price_list == False:
                product.print_info()
        
        # Prompt user for normal price input for those product
        for product in item_list:

            if product.in_normal_price_list == False:
                print("\n")
                print(f"Plug in estimated normal price for, {product.model}:")
                estimated_normal_price = float(input())
                product.normal_price = estimated_normal_price * product.unit
        
        # prompt decision before compute final data
        # Show user how many are item without normal price
        product_not_in_normal_price_list_counter = 0

        for product in item_list:

            if product.in_normal_price_list == False:
                product_not_in_normal_price_list_counter += 1
        
        item_list_length = len(item_list)

        print("\n")
        print(product_not_in_normal_price_list_counter, "out of", item_list_length, "does not have a normal price")

        print(f"""
        Enter 
        1: Compute final data with newly estimated normal price, 
        2: Compute final data with only available normal price """)

        user_decision = int(input())

        if user_decision == 1:
            
            current_deliverables = 0

            for product in item_list:

                if product.in_normal_price_list == True:
                    current_deliverables += product.estimated
                else:
                    current_deliverables += product.normal_price

            total_deliverables = (current_deliverables * 109) + region_monthly_performance.revenue

            for item in item_list:
                if item.in_normal_price_list == False:
                    item.print_info()

            print(f"\n")
            print(f"deliverables: {current_deliverables:,}")
            print(f"total_expected_deliverables: {total_deliverables:,}")
            print(f"\n")
        
        else:
            current_deliverables = 0

            for product in item_list:

                if product.in_normal_price_list == True:
                    current_deliverables += product.estimated

            total_deliverables = (current_deliverables * 109) + region_monthly_performance.revenue


            for item in item_list:
                if item.in_normal_price_list == False:
                    item.print_info()

            print(f"\n")
            print(f"deliverables: {current_deliverables:,}")
            print(f"total_expected_deliverables: {total_deliverables:,}")
            print(f"\n")




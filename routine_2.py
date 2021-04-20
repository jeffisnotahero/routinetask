# Date: 28/03/2021
# Description: Automate routine task from work
#              Compute forecasted revenue & booking performance(few days before next month) and display the output

import csv
import sys
from helper import *

# Check length of Command-line argument 
if len(sys.argv) > 5 or len(sys.argv) < 4:
    print(f"""
                                            ----MUST FOLLOW THE ORDER OF INPUT OF CSV FILE!!!---- 
        Usage: python routine.py 'DELIVERABLES'.csv, 'DSICOUNT PRICE LIST'.csv, 'NORMAL PRICE LIST'.csv, 'REVENUE AS OF NOW'.csv for Korea data;
        Usage: python routine.py 'DELIVERABLES'.csv, 'NORMAL PRICE LIST'.csv, 'REVENUE AS OF NOW'.csv for China data
                                            ----MUST FOLLOW THE ORDER OF INPUT OF CSV FILE!!!---- 
        \n""")
    sys.exit(1)

# Prompt user to choose which region data to be computed
incoming_computed_data = int(input("Enter 1 if Korea data, Enter 2 if China data \n"))

# Handling Korea region data
if incoming_computed_data == 1:

    # Create deliverable model name list
    item_name_list = create_item_name_list(sys.argv[1])

    # Create deliverable objects with each name from the model name list
    product_list = []
    for name in item_name_list:
        product_list.append(Deliverables(name))

    # Add unit data for each deliverable
    add_deliverables_unit_data(sys.argv[1], product_list)

    # Add discount price for each deliverables 
    add_discount_price(sys.argv[2], product_list)

    # Add normal price for each deliverables 
    add_normal_price(sys.argv[3], product_list)

    # Compute total revenue data for region as of now
    region_monthly_performance = Region("Region_monthly_performance")
    compute_revenue_data(sys.argv[4], region_monthly_performance)
    region_monthly_performance.print_info()

    # Compute the total deliverables if only each deliverables have their discount price
    is_discount_price_list_counter = check_all_deliverables_with_required_price(product_list, "in_discount_price_list")
    if is_discount_price_list_counter == 0:
        
        compute_total_deliverables_if_all_with_required_price(product_list, "estimated", region_monthly_performance)

    # Otherwise, compute the total deliverables with estimated discount price plugged in manually.
    else:

        # Plug in estiamted discount price for each deliverables that does not have discount price
        prompt_user_plug_in_estimated_discount_price(product_list)

        # Prompt user to make a decision of computation of data
        check_total_numbers_unavailable_normal_or_discount_price(product_list, "in_discount_price_list")

        print(f"""
        Enter 
        1: Compute final data with available and newly estimated discount price, 
        2: Compute final data with only available discount price """)

        # Compute the corresponding final data based on user's decision
        compute_final_data_based_on_input_selection(product_list, "in_discount_price_list", "estimated", region_monthly_performance)

# Handling China region data
else:
    # Create deliverable model name list
    item_name_list = create_item_name_list(sys.argv[1])

    # Create deliverable objects with each name from the model name list
    product_list = []
    for name in item_name_list:
        product_list.append(Deliverables(name, in_discount_price_list=False))

    # Add unit data for each deliverable
    add_deliverables_unit_data(sys.argv[1], product_list)

    # Add discount price for each deliverables 
    add_normal_price(sys.argv[2], product_list)

    # Compute total revenue data for region as of now
    region_monthly_performance = Region("Region_monthly_performance")
    compute_revenue_data(sys.argv[3], region_monthly_performance)
    region_monthly_performance.print_info()

    # Compute the total deliverables if only each deliverables have their discount price

    is_normal_price_list_counter = check_all_deliverables_with_required_price(product_list, "in_normal_price_list")
    if is_normal_price_list_counter == 0:
        
        compute_total_deliverables_if_all_with_required_price(product_list, "normal_price", region_monthly_performance)

    # Otherwise, compute the total deliverables with estimated discount price plugged in manually.
    else:
        
        # Plug in estiamted normal price for each deliverables that does not have normal price 
        prompt_user_plug_in_estimated_normal_price(product_list)

        # Prompt user to make a decision of computation of data
        check_total_numbers_unavailable_normal_or_discount_price(product_list, "in_normal_price_list")
        
        print(f"""
        Enter 
        1: Compute final data with available and newly estimated normal price, 
        2: Compute final data with only available normal price """)

        # Compute the corresponding final data based on user's decision
        compute_final_data_based_on_input_selection(product_list, "in_normal_price_list", "normal_price", region_monthly_performance)

        # For total deliverabels, show profit data
        # Show booking data

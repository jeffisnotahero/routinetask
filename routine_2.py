# Date: 28/03/2021
# Description: Automate routine task from work
#              Compute forecasted revenue & booking performance(few days before next month) and display the output

import csv
import sys
from helper import *

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

    # Create item object and insert into list
    product_list = []
    for name in item_name_list:
        product_list.append(Deliverables(name))

    # Add deliverables unit data 
    add_deliverables_unit_data(sys.argv[1], product_list)

    # Add discount price
    add_discount_price(sys.argv[2], product_list)

    # Add normal price
    add_normal_price(sys.argv[3], product_list)

    # Compute revenue data as of now
    region_monthly_performance = Region("Region_monthly_performance")
    compute_revenue_data(sys.argv[4], region_monthly_performance)
    region_monthly_performance.print_info()

    # Check if everything has discount price and compute immediately
    is_discount_price_list_counter = check_all_deliverables_with_required_price(product_list, "in_discount_price_list")

    if is_discount_price_list_counter == 0:
        
        compute_total_deliverables_if_all_with_required_price(product_list, "estimated", region_monthly_performance)

    # else handling
    else:

        # Check and plug in estiamted discount price for those products without 
        prompt_user_plug_in_estimated_discount_price(product_list)

        # prompt decision before compute final data
        # Show user how many are item without normal and discount as well as item without discount only
        check_total_numbers_unavailable_normal_or_discount_price(product_list, "in_discount_price_list")

        print(f"""
        Enter 
        1: Compute final data with available and newly estimated discount price, 
        2: Compute final data with only available discount price """)

        compute_final_data_based_on_input_selection(product_list, "in_discount_price_list", "estimated", region_monthly_performance)

# Handle China data
else:
    # Create item list
    item_name_list = create_item_name_list(sys.argv[1])

    # Create item object and insert into list
    product_list = []
    for name in item_name_list:
        product_list.append(Deliverables(name, in_discount_price_list=False))

    # Add deliverables unit data
    add_deliverables_unit_data(sys.argv[1], product_list)

    # Add normal price
    add_normal_price(sys.argv[2], product_list)

    # Compute revenue data as of now
    region_monthly_performance = Region("Region_monthly_performance")
    compute_revenue_data(sys.argv[3], region_monthly_performance)
    region_monthly_performance.print_info()

    # if everything has normal price compute immediately

    is_normal_price_list_counter = check_all_deliverables_with_required_price(product_list, "in_normal_price_list")

    if is_normal_price_list_counter == 0:
        
        compute_total_deliverables_if_all_with_required_price(product_list, "normal_price", region_monthly_performance)

    # else handling
    else:
        
        # Check and plug in estiamted normal price for those products without 
        prompt_user_plug_in_estimated_normal_price(product_list)

        # prompt decision before compute final data
        # Show user how many are item without normal price
        check_total_numbers_unavailable_normal_or_discount_price(product_list, "in_normal_price_list")

        print(f"""
        Enter 
        1: Compute final data with available and newly estimated normal price, 
        2: Compute final data with only available normal price """)

        compute_final_data_based_on_input_selection(product_list, "in_normal_price_list", "normal_price", region_monthly_performance)

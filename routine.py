# Date: 28/03/2021
# Description: Automate routine task from work

# <Features>
# 1. Compute data, output to new csv file and display as output as below
#     1. 3 Distributors & Other's
#         1. Booking data
#         2. Revenue data
#         3. Cost data
#         4. Net sales data
#         5. Net profit margin data
#     2. Monthly Booking (Total)
#     3. Monthly Revenue (Total)
#         1. Cost
#         2. Net sales
#         3. Net profit margin
# 2. Check if there is date (出荷日) later than current date when the data downloaded, or current date  in the table

import csv
import sys
from helper import *

# Check command-line argument
if len(sys.argv) != 3:
    print("Usage: python routine.py 'YOUR REVENUE CSV'.csv 'YOUR BOOKING CSV'.csv ----MUST FOLLOW THE ORDER OF CSV FILE!!!----")
    sys.exit(1)

# Create Object for 3 distributors & Other & Region
m_monthly_performance = Distributor("m_monthly_performance", 0, 0, 0, 0, 0)
t_monthly_performance = Distributor("t_monthly_performance", 0, 0, 0, 0, 0)
n_monthly_performance = Distributor("n_monthly_performance", 0, 0, 0, 0, 0)
o_monthly_performance = Distributor("o_monthly_performance", 0, 0, 0, 0, 0)
region_monthly_performance = Region("region_monthly_performance", 0, 0, 0, 0, 0)

# Open revenue CSV and read everything into memory
with open(sys.argv[1], "r", encoding="shift_jis") as database:

    # row[0] : "distributor"
    # row[12] : "revenue"
    # row[13] : "cost"
    revenue_data = csv.reader(database)

    # Skip first row (Description row)
    next(revenue_data)

    list_revenue_data = list(revenue_data)
    
    # Compute Monthly Distributors' Revenue & Cost data
    for row in list_revenue_data:

        # Update each distributors' data
        if row[0] == "10590|Maintech":    
            update_revenue_and_cost(m_monthly_performance, row)
        
        elif row[0] == "10601|TST":    
            update_revenue_and_cost(t_monthly_performance, row)

        elif row[0] == "ｴ9905|N.C. Tech":    
            update_revenue_and_cost(n_monthly_performance, row)
        
        else:
            update_revenue_and_cost(o_monthly_performance, row)

    all_distributor_list = [m_monthly_performance, t_monthly_performance, n_monthly_performance, o_monthly_performance] # List guaranteed to be iterated in order

    # Compute each distributors' Net sales data & Net profit margin
    for distributor in all_distributor_list:

        distributor_net_sales = compute_net_sales(distributor) # Compute distributors' Net sales
        update_net_sales(distributor, distributor_net_sales) # Update distributors' Net sales

        distributor_net_profit_margin_non_percentage = compute_net_profit_margin(distributor) # Compute distributtors' Net profit margin
        distsributor_net_profit_margin = format_value_with_percentage(distributor_net_profit_margin_non_percentage) # Format value with percentage
        update_net_profit_margin(distributor, distsributor_net_profit_margin) # Update distributors' Net profit margin

    # Compute Region Monthly Total Booking
    for row in list_revenue_data:

        update_revenue_and_cost(region_monthly_performance, row)
    
    region_net_sales = compute_net_sales(region_monthly_performance) # Compute Region's Net sales
    update_net_sales(region_monthly_performance, region_net_sales) # Update Region's Net sales

    region_net_profit_margin_non_percentage = compute_net_profit_margin(region_monthly_performance) # Compute Region's Net profit margin
    region_net_profit_margin = format_value_with_percentage(region_net_profit_margin_non_percentage) # Format value with percentage
    update_net_profit_margin(region_monthly_performance, region_net_profit_margin) # Update Region's Net profit margin

# Open booking CSV and read everything into memory
with open(sys.argv[2], "r", encoding="shift_jis") as database:

    # row[0] : "distributor"
    # row[12] : "booking"
    # row[13] : "cost"
    booking_data = csv.reader(database)

    # Skip first row (Description row)
    next(booking_data)

    list_booking_data = list(booking_data)

    # Compute Monthly Distributors' Revenue & Cost data
    for row in list_booking_data:

        # Update each distributors' data
        if row[0] == "10590|Maintech":    
            update_booking(m_monthly_performance, row)
        
        elif row[0] == "10601|TST":    
            update_booking(t_monthly_performance, row)

        elif row[0] == "ｴ9905|N.C. Tech":    
            update_booking(n_monthly_performance, row)
        
        else:
            update_booking(o_monthly_performance, row)

    # Compute Region Monthly Total Booking
    for row in list_booking_data:

        update_booking(region_monthly_performance, row)
    
    # Print Region & Distributors' data
    region_monthly_performance.print()
    m_monthly_performance.print()
    t_monthly_performance.print()
    n_monthly_performance.print()
    o_monthly_performance.print()
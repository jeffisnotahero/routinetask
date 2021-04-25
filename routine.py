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

import csv
import sys
from helper import *

# Check command-line argument
if len(sys.argv) != 3:
    print("Usage: python routine.py 'YOUR REVENUE CSV'.csv 'YOUR BOOKING CSV'.csv ----MUST FOLLOW THE ORDER OF INPUT OF CSV FILE!!!----")
    sys.exit(1)

# Create name list
name_list = create_name_list(sys.argv[1], sys.argv[2])

# Create distributor list
distributor_list = []

for name in name_list:
    distributor_list.append(Distributor(name))

# Region monthly performance object
region_monthly_performance = Region("Region_monthly_performance")

# Open revenue CSV and read everything into memory
list_revenue_data = compute_revenue_list(sys.argv[1])
    
# Compute Monthly Distributors' Revenue & Cost data
for distributor in distributor_list:

    for row in list_revenue_data:

        # Update each distributors' data
        if row[0] == distributor.name:    
            update_revenue_and_cost(distributor, row)

# Compute each distributors' Net sales data & Net profit margin
for distributor in distributor_list:

    distributor_net_sales = compute_net_sales(distributor) # Compute distributors' Net sales
    update_net_sales(distributor, distributor_net_sales) # Update distributors' Net sales

    distributor_net_profit_margin_non_percentage = compute_net_profit_margin(distributor) # Compute distributtors' Net profit margin
    distsributor_net_profit_margin = format_value_with_percentage(distributor_net_profit_margin_non_percentage) # Format value with percentage
    update_net_profit_margin(distributor, distsributor_net_profit_margin) # Update distributors' Net profit margin

# Compute Region Monthly Total Revenue
compute_revenue_data(sys.argv[1], region_monthly_performance)

# Open booking CSV and read everything into memory
list_booking_data = compute_booking_list(sys.argv[2])

# Compute Monthly Distributors' Revenue & Cost data
for distributor in distributor_list:

    for row in list_booking_data:

        # Update each distributors' data
        if row[0] == distributor.name:    
            update_booking(distributor, row)

# Compute Region Monthly Total Booking
for row in list_booking_data:

    update_booking(region_monthly_performance, row)

# Print all region & distributor info
for distributor in distributor_list:
    distributor.print_info()

region_monthly_performance.print_info()
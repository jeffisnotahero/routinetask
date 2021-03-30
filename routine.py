# Date: 28/03/2021
# Description: Automate routine task from work

# <Features>
# 1. Compute data and display as output as below
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
# 1st argv => csv
if len(sys.argv) != 3:
    print("Usage: python routine.py 'YOUR REVENUE CSV'.csv 'YOUR BOOKING CSV'.csv ----MUST FOLLOW THE ORDER OF CSV FILE!!!----")
    sys.exit(1)

# Create Object for 3 distributors & Other
m_monthly_performance = Distributor("m_monthly_performance", 0, 0, 0, 0, 0)
t_monthly_performance = Distributor("t_monthly_performance", 0, 0, 0, 0, 0)
n_monthly_performance = Distributor("n_monthly_performance", 0, 0, 0, 0, 0)
o_monthly_performance = Distributor("o_monthly_performance", 0, 0, 0, 0, 0)

# Create Object for Region
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
        if row[0] == "10590|M":    
            update_revenue_and_cost(m_monthly_performance, row)
        
        elif row[0] == "10601|T":    
            update_revenue_and_cost(t_monthly_performance, row)

        elif row[0] == "ｴ9905|N":    
            update_revenue_and_cost(n_monthly_performance, row)
        
        else:
            update_revenue_and_cost(o_monthly_performance, row)

    print(f"""
    m_monthly_performance revenue:{m_monthly_performance.revenue}
    t_monthly_performance revenue:{t_monthly_performance.revenue} 
    n_monthly_performance revenue:{n_monthly_performance.revenue} 
    o_monthly_performance revenue:{o_monthly_performance.revenue} 
    
    m_monthly_performance cost:{m_monthly_performance.cost}
    t_monthly_performance cost:{t_monthly_performance.cost} 
    n_monthly_performance cost:{n_monthly_performance.cost} 
    o_monthly_performance cost:{o_monthly_performance.cost} 
    """)

    all_distributor_list = [m_monthly_performance, t_monthly_performance, n_monthly_performance, o_monthly_performance] # List guaranteed to be iterated in order

    # Compute each distributors' Net sales data & Net profit margin
    for distributor in all_distributor_list:
        
        print(distributor)

        # Compute distributors' Net sales
        distributor_net_sales = compute_net_sales(distributor)

        # Update distributors' Net sales
        update_net_sales(distributor, distributor_net_sales)

        print(distributor_net_sales)
        print(distributor.net_sales)

        # Compute distributtors' Net profit margin
        distributor_net_profit_margin_non_percentage = compute_net_profit_margin(distributor)

        # Format value with percentage
        distsributor_net_profit_margin = format_value_with_percentage(distributor_net_profit_margin_non_percentage)

        # Update distributors' Net profit margin
        update_net_profit_margin(distributor, distsributor_net_profit_margin)


        print(distsributor_net_profit_margin)
        print(distributor.net_profit_margin)

    # Compute Region Monthly Total Booking
    for row in list_revenue_data:

        update_revenue_and_cost(region_monthly_performance, row)
    
    # Compute Region's Net sales
    region_net_sales = compute_net_sales(region_monthly_performance)

    # Update Region's Net sales
    update_net_sales(region_monthly_performance, region_net_sales)

    # Compute Region's Net profit margin
    region_net_profit_margin_non_percentage = compute_net_profit_margin(region_monthly_performance)

    # Format value with percentage
    region_net_profit_margin = format_value_with_percentage(region_net_profit_margin_non_percentage)

    # Update Region's Net profit margin
    update_net_profit_margin(region_monthly_performance, region_net_profit_margin)

    print(region_monthly_performance.revenue) 
    print(region_monthly_performance.cost) 
    print(region_monthly_performance.net_profit_margin)

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

    print(f"""
    m_monthly_performance booking:{m_monthly_performance.booking}
    t_monthly_performance booking:{t_monthly_performance.booking} 
    n_monthly_performance booking:{n_monthly_performance.booking} 
    o_monthly_performance booking:{o_monthly_performance.booking} 
    """)

    # Compute Region Monthly Total Booking
    for row in list_booking_data:

        update_booking(region_monthly_performance, row)
    
    print(region_monthly_performance.booking)
    
    
    # -Loop every booking amount row of booking CSV
    #     -update booking's total_amount property
        
    # -Print out all monthly Booking & Revenue's total amount, cost, Net sales data & Net profit margin
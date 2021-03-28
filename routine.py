# Date: 28/03/2021
# Description: Automate routine task from work

# <Features>
# 1. Calculate data and display as output as below
#     1. 3 Distributors & Other's
#         1. Booking data
#         2. Revenue data
#         3. Cost data
#         4. Profit data
#         5. Profit rate data
#     2. Monthly Booking (Total)
#     3. Monthly Revenue (Total)
#         1. Cost
#         2. Profit
#         3. Profit rate
# 2. Check if there is date (出荷日) later than current date when the data downloaded, or current date  in the table

# Logic & pseudocode

    # //Calculate 3 distributors & Other's data//
    # -Open revenue CSV and read everything into memory

    # -Create distributor Class for 3 distributors & Other with Booking, Revenue, Cost, Profit, Profit rate properties
    # -Create Object for 3 distributors & Other
    # -Loop every row of CSV
    #     -if A distributors
    #         -Assign Booking, Revenue, Cost, Profit values by modifying A distributor properties

    #     -elif B
    #         -Assign...by modifying...

    #     -elif C
    #         -Assign...by modifying...

    #     -else
    #         -Assign...by modifying...
    #             -Calculate profit rate
    
    # -Create objects array with 3 distributor Objects
    #     -Loop through it
    #         -Calculate profit date
    #             -Profit date = Revenue - Cost
    #             -update distributor's profit data property

    #         -Calculate profit rate
    #             -Profit rate = profit date / total_revenue
    #             -Assign profit rate by modifying profit rate properties

    # -Print out all Booking, Revenue, Cost, Profit, Profit rate value for 3 distributors and Other

    #  //Calculate Monthly total Booking & Revenue//
    # -Open booking CSV and read everything into memory

    # -Create monthly_performance Parent Class with total_amount, cost, profit, profit rate properties
    # -Create revenue & booking Child Class
    # -Create Object for revenue & booking

    # -Loop every revenue, cost amount row of revenue CSV
    #     -update revenue's total_amount, cost property

    # -Calculate profit date
    #     -Profit date = Revenue - Cost
    #     -update revenue's profit data property

    # -Calculate profit rate
    #     -Profit rate = profit date / total_revenue
    #     -Assign profit rate by modifying profit rate properties
        
    # -Loop every booking amount row of booking CSV
    #     -update booking's total_amount property
    
    # -Print out all monthly Booking & Revenue's total amount, cost, profit data & profit rate
    
        

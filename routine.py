# Date: 28/03/2021
# Description: Automate routine task from work

# <Features>
# 1. Calculate data and display as output as below
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

# Logic & pseudocode

    # //Calculate 3 distributors & Other's data//
    # -Open revenue CSV and read everything into memory

    # -Create distributor Class for 3 distributors & Other with Booking, Revenue, Cost, Net sales, Net profit margin properties
    # -Create Object for 3 distributors & Other
    # -Loop every row of CSV
    #     -if A distributors
    #         -Assign Booking, Revenue, Cost, Net sales values by modifying A distributor properties

    #     -elif B
    #         -Assign...by modifying...

    #     -elif C
    #         -Assign...by modifying...

    #     -else
    #         -Assign...by modifying...
    #             -Calculate Net profit margin
    
    # -Create objects array with 3 distributor Objects
    #     -Loop through it
    #         -Calculate Net sales data
    #             -Net sales data = Revenue - Cost
    #             -update distributor's Net sales data property

    #         -Calculate Net profit margin
    #             -Net profit margin = Net profit date / total_revenue
    #             -Assign Net profit margin by modifying Net profit margin properties

    # -Print out all Booking, Revenue, Cost, Net sales, Net profit margin value for 3 distributors and Other

    #  //Calculate Monthly total Booking & Revenue//
    # -Open booking CSV and read everything into memory

    # -Create monthly_performance Parent Class with total_amount, cost, Net profit, Net profit margin properties
    # -Create revenue & booking Child Class
    # -Create Object for revenue & booking

    # -Loop every revenue, cost amount row of revenue CSV
    #     -update revenue's total_amount, cost property

    # -Calculate Net sales data
    #     -Net sales data = Revenue - Cost
    #     -update revenue's Net sales data property

    # -Calculate Net profit margin
    #     -Net profit margin = Net sales data / total_revenue
    #     -Assign Net profit margin by modifying Net profit margin properties
        
    # -Loop every booking amount row of booking CSV
    #     -update booking's total_amount property
    
    # -Print out all monthly Booking & Revenue's total amount, cost, Net sales data & Net profit margin
    
import csv
import sys

# # Check command-line argument
# # 1st argv => csv
# if len(sys.argv) != 2:
#     print("Usage: python routine.py 'YOUR CSV'.csv")
#     sys.exit(1)

# Open CSV and read everything into memory
with open(sys.argv[1], "r", encoding='shift_jis') as database:
    data = csv.reader(database)

    # Skip first row (description)
    next(data)
    for row in data:
        content = row[12]
        print (content)

# Create Distributor class
class Distributor:
    def __init__(self, booking, revenue, cost, net_sales, net_profit_margin):
        self.booking = booking
        self.revenue = revenue
        self.cost = cost
        self.net_sales = net_sales
        self.net_profit_margin = net_profit_margin

# Create Object for 3 distributors & Other
m = Distributor(0, 0, 0, 0, 0)
t = Distributor(0, 0, 0, 0, 0)
n = Distributor(0, 0, 0, 0, 0)


# Loop every row of CSV
#     -if A distributors
#         -Assign Booking, Revenue, Cost, Net sales values by modifying A distributor properties

#     -elif B
#         -Assign...by modifying...

#     -elif C
#         -Assign...by modifying...

#     -else
#         -Assign...by modifying...
#             -Calculate Net profit margin
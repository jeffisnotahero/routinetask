Logic & pseudocode

    //Compute 3 distributors & Other's data//
    -Open revenue CSV and read everything into memory
    -Open booking CSV and read everything into memory

    -Create Parent class for Booking, Revenue, Cost, Net sales, Net profit margin properties
    -Create child Class for 3 distributors & Other with Booking, Revenue, Cost, Net sales, Net profit margin properties
    -Create Object for 3 distributors & Other
    -Loop every row of CSV
        -if A distributors
            -Assign Booking, Revenue, Cost, Net sales values by modifying A distributor properties

        -elif B
            -Assign...by modifying...

        -elif C
            -Assign...by modifying...

        -else
            -Assign...by modifying...
    
    -Create objects array with 3 distributor Objects
        -Loop through it
            -Compute Net sales data
                -Net sales data = Revenue - Cost
                -update distributor's Net sales data property

            -Compute Net profit margin
                -Net profit margin = Net sales data / total_revenue
                -Assign Net profit margin by modifying Net profit margin properties

    -Print out all Booking, Revenue, Cost, Net sales, Net profit margin value for 3 distributors and Other

     //Compute Monthly total Booking & Revenue//

    -Create revenue & booking Child Class
    -Create Object for revenue & booking

    -Loop every revenue, cost amount row of revenue CSV
        -update revenue's total_amount, cost property

    -Compute Net sales data
        -Net sales data = Revenue - Cost
        -update revenue's Net sales data property

    -Compute Net profit margin
        -Net profit margin = Net sales data / total_revenue
        -Assign Net profit margin by modifying Net profit margin properties
        
    -Loop every booking amount row of booking CSV
        -update booking's total_amount property
    
    -Print out all monthly Booking & Revenue's total amount, cost, Net sales data & Net profit margin
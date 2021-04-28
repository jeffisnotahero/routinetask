Author: Wang Wai Siong    
Date: 29 March 2021  
Description: Pseudocode for factoring the logic and code of routine project  

    //Compute 3 distributors & Other's data//
    -Open revenue CSV and read everything into memory
    -Open booking CSV and read everything into memory

    -Create Parent class for Booking, Revenue, Cost, Net sales, Net profit margin properties
    -Create child Class for 3 distributors & Other with Booking, Revenue, Cost, Net sales, Net profit margin properties
    -Create Object for 3 distributors & Other

    -Get all names from file and insert it to a list
    -Create a name list

    -Loop every 0 row (name row) [names from revenue.csv]
        -Loop every items in the list
            -if name of current row in the name list
                -break the loop
            -else
                -add the name into the name list

    -Loop every 0 row (name row) [names from booking.csv]
        -Loop every items in the list
            -if name of current row in the name list
                -break the loop
            -else
                -add the name into the name list
        
    -Create a object list
    -Loop every name list
        -creating object with current name and insert into object list

    -Loop every distributor object list
        -Loop every row of CSV
            -if current row name same as current distributor name
                -Assign Booking, Revenue, Cost, Net sales values by modifying current distributor properties
        
            -Compute Net sales data
                -Net sales data = Revenue - Cost
                -update distributor's Net sales data property

            -Compute Net profit margin
                -Net profit margin = Net sales data / total_revenue
                -Assign Net profit margin by modifying Net profit margin properties
    
    -Loop every row of revenue csv
        -update region revenue object
    -Compute Net sales data
    -Compute Net profit margin

    -Print out all Booking, Revenue, Cost, Net sales, Net profit margin value for 3 distributors and Other

     //Compute Monthly total Booking for region and distributor//

    -Loop distributor from distributor list
  
        -Loop every booking amount row of booking CSV
            -if current row name is same as current distributor name
                -update booking's total_amount property
    
    -Loop every row of booking csv
        -update region booking object
        
        
    -Print out all monthly Booking & Revenue's total amount, cost, Net sales data & Net profit margin
Author: Wang Wai Siong  
Date: 14 April 2021  
Description: Pseudocode for a program that takes differnt region's monthly booking and revenue csv file as input,
             and show the product, which its booking and revenue amount is equal or more than 500k JPY,
             its model, net sales, net profit margin, customer order number and order date

Pre-condition:
Prepare a list for China, which includes orders that is more than or equal to 500k JPY, from orders CC-ed to me, with content below
    -distributor
    -customer name
    -product model
    -order date
    -customer order number
    -booking


-Prepare a list for Korea with content below from project list
    -distributor
    -customer name
    -product model
    -application


Korea, China region revenue requirements:
1) First get data below, revenue that is more than or equal to 500k JPY,
    distributor
    product model
    order date
    customer order number
    revenue
    cost
    net sales
    net profit margin

2) Insert into the monthly report and insert the customer name data based on record made in prior

Korea and China region booking requirements:
1) Same steps with China region revenue requirements
2) However, when getting data for more than or equal to 500k JPY,
   check if there is same orders, with the booking that more than or equal to 500k JPY,
   have minus amount.
3) If so exclude the order as it is merely adjustment of changes of currency rate.

PSEUDOCODE

    Define a new class-over_500k_orders & over_500k_revenues that includes properties below (by inheriting Parent class-monhtly performance)
        over_500k_revenues: 
            distributor
            product model
            order date
            customer order number
            revenue
            cost
            net sales
            net profit margin

            print self name

            print info

        over_500k_orders:
            distributor
            product model
            order date
            customer order number
            booking
            cost
            net sales
            net profit margin
            is_currency_adjustment = False

            print self name

            print info


    Populate Revenue data:
        -open revenue csv
        -create over_500k_revenue_list
        -loop the revenue csv
            -if revenue >= 500k:
                -append over_500k_revenue_list with (over_500k_revenues object( distributor, product model, order date, customer order number, revenue, cost))
                -compute net sales & update net sales
                -compute net profit margin & update net profit margin

        -loop over_500k_revenue_list
            -print all info

        -create over_500k_booking_list
        -loop the booking csv
            -if booking >= 500k 
                -append over_500k_booking_list with (over_500k_booking object( distributor, product model, order date, customer order number, booking, cost))
                -compute net sales & update net sales
                -compute net profit margin & update net profit margin

            -if booking <= -500k 
                -append over_500k_booking_list with (over_500k_booking object( distributor, product model, order date, customer order number, booking, cost))

        -create a list of order number with positive booking amount orders

        -create a list of order number that is not for currency adjustment
        
        -loop through list of order number
            - amount_list = [booking amount ; loop through list booking data ; if order number in list] booking data
                -loop through amount list
                    -total = 0
                    -total += amount
                
                if total_amount > 0
                    -add this order number into the corresponding list
        
        -create a list of booking data that is not for currency adjustmnet

        # distributor, product model
        -loop through list of order number that is not for currency adjustment
            -while currenct order number != order number from extract booking data list
                -loop through extract booking data list
                    -if current order number == order number from extract booking data list
                        -append list(booking data non currency adjustment) by adding Booking(distributor,product model)
            
        # order date
        -loop through list of order number that is not for currency adjustment
            -current date = 0
            -loop through extract booking data list
                -if order number == order number from extract booking data list
                    if booking data order data > current date
                        current date = booking data order data
            
            -loop through booking data non currency adjustment list
                -if order number == order number from booking data non currency adjustment list
                    -current order date =  current date

        # booking, cost, unit
        -loop through list of order number that is not for currency adjustment
            -booking = 0
            -booking cost = 0
            -unit = 0
            -loop through extract booking data list
                -if currenct order number == order number from extract booking data list
                    -booking += booking
                    -booking cost += booking cost
                    -unit += unit
            
            -loop through booking data non currency adjustment list
                -if order number == order number from booking data non currency adjustment list
                    -current order number booking = booking
                    -current order number booking cost = booking cost
                    -current order number unit = unit    

            -booking = 0
            -booking cost = 0
            -unit = 0


        -loop over_500k_booking_list
            -if both is_currency_adjustnment == False
                -print info
        

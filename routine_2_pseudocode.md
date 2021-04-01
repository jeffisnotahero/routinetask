--Compute forecasted revenue & booking performance(few days before next month) and display the output--

-price list data
-delivery data of rest of month as of current date

-delivery item class
    -item.name
    -item.unit
    -item.estimated
    -item.boolean.check_if_in_price

    -print_info function
        if item.boolean.check_if_in_price is true
            -print all info
        else
            -print not in price list
            -print all info

-import delivery data
    -create a product name list

-create item list

-loop the item list 
    -loop the price list
        -if same product name with items from price list
            -compute estimated and update item estimated
        -else
            -change item.boolean.check_if_in_price to true

-loop item list
    -print all info

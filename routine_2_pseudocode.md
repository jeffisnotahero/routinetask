--Compute forecasted revenue & booking performance(few days before next month) and display the output--

-discount price list data
-delivery data of rest of month as of current date

-delivery item class
    -item.name
    -item.unit
    -item.estimated
    -item.cost
    -item.boolean.check_if_in_discount_price_list =default true
    -item.boolean.check_if_in_normal_price_list =default true

    -print_info function
        if item.boolean.check_if_in_price is true
            -print all info
        else
            -print not in discount price list
            -print all info

-import delivery data
    -create a product name list

-create item list and objects 
-add units to each item from list

// check every item could be priced with discount list and normal list and label it
-loop the item list 
    -loop the discount price list
        -if same product name with items from discount price list
            -compute estimated and update item estimated
        -else
            -change item.boolean.check_if_in_price to false

    -loop the normal price list
        -if there is no same product name with items from normal price list
            -change item.boolean.check_if_in_normal_price to false

// action taken in prior for what if there is items cannot be priced in normal price list
-loop the item list
    -show how many are there
    -prompt user to provide input(estimated) & cost for those items amd update those item

-compute total revenue & cost as of now

// prompt decision before compute final data
-loop item list

    -if there is item.booleam.check_if_in_discount_price_false
        -print how many are there and those info
        -prompt user if they want compute those with normal price or not and show output
            -if true
                -loop normal price and compute estimated & cost and update those item estimated & cost

                -loop items list, sum total revenue and delivery amount, compute net profit margin and show output
            -else
                -loop item list, sum delivery amount (item boolean check = true), compute net profit margin and show output
                -print those item that not existed in the discount list
    
    -else
        -loop item list, sum every delivery amount (item boolean check = true), compute net profit margin and show output
        -print those item
        -print all items in discount list


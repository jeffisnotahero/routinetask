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

-check argument line
    -if argument > 3
        -prompt user to provide correct argument

-prompt user which types date to compute
    -if 1 =>  Korea:

        -import delivery data with input argument
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

        -compute total revenue & cost as of now

        // if everything has discount price compute immediately
        -loop item list:
            counter = 0
            if item is discount price = false
            counter + 1
        if counter = 0:
            -loop item list:
                compute total deliverables
            sum total revenue & deliverables

        else:
            // Check if item.booleam.check_if_in_normal_price_false and
            -loop the item list
                -show how many are there
                -prompt user to provide input(estimated) & cost for those items amd update those item OR skip


            // Check if item.booleam.check_if_in_discount_price_false and
            -loop item list
                -show how many are there
                -prompt user to provide input(estimated) & cost for those items amd update those item OR skip


            // prompt decision before compute final data
            // show user how many are item without normal and discount as well as item without discount only
            -loop item list
                -if item_normal_list AND item_discount_list is true:
                    Acounter +1
                
                -if item_normal_list is true and item_discount_list is false:
                    Bcounter +1

                -if item_normal_list is false and item_discount_list is true:
                    Ccounter +1

            print all type of counter

            -prompt user if they want to continue to compute all data with later added data
                -if true (usually scenario where later added price is fine)
                    -deliverables = 0
                    -loop item list
                        -if item is in discount list true
                            -deliverables += item.estimated
                        else
                            -deliverables += item.normal price

                -else:
                    -deliverables = 0
                    -loop item list
                        -if item is in discount list true
                            -deliverables += item.estimated

                - total expected deliverable = deliverables + total revenue


    else: (CSL data)

        -import delivery data with input argument
            -create a product name list

        -create item list and objects 
        -add units to each item from list

        // check every item could be priced with normal list and label it
        -loop the item list 
            -loop the normal price list
                -if same product name with items from normal price list
                    -compute estimated and update item estimated
                -else
                    -change item.boolean.check_if_in_normal_price to false

        -compute total revenue & cost as of now

        // if everything has normal price compute immediately
        -loop item list:
            counter = 0
            if item is normal price = false
            counter + 1
        if counter = 0:
            -loop item list:
                compute total deliverables
            sum total revenue & deliverables

        else:
            // Check if item.booleam.check_if_in_normal_price_false and
            -loop the item list
                -show how many are there
                -prompt user to provide input(estimated) & cost for those items amd update those item 

            // prompt decision before compute final data
            // show user how many are item without normal price list
            -loop item list
                -if item_normal_list is true:
                    Acounter +1

            print all type of counter

            -prompt user if they want to continue to compute all data with later added data
                -if true (usually scenario where later added price is fine)
                    -deliverables = 0
                    -loop item list
                        -if item is in normal price list true and false
                            -deliverables += item.estimated
                -else:
                    -deliverables = 0
                    -loop item list
                        -if item is in normal price list true
                            -deliverables += item.estimated

                - total expected deliverable = deliverables + total revenue





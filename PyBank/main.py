import csv

with open('./Resources/budget_data.csv', 'r') as file:

    # reading in data
    data = csv.reader(file, delimiter = ',')

    #skipping annd saving header row
    header = next(data)

    prev_month_str = '' # temp variable to hold last month recorded
    total_months = 0 # variable to track number of months recorded

    total_profits = 0 # keeps track of total profits
    first_month_val = 0 # holds profits/losses of first month
    last_month_val = 0 # holds profits/losses of last month

    prev_month_val = 0
    cur_month_val = 0

    greatest_inc_val = 0
    greatest_inc_str = ''
    greatest_dec_val = 0
    greatest_dec_str = ''

    counter = 0

    # iterating through rows
    for row in data:

        # if we've encountered data for a new month
        if row[0] != prev_month_str:
            prev_month_str = row[0] # update the month's name info
            total_months += 1 # increment the number of months by 1

        # if we're on the first row
        if counter == 0:
            first_month_val = float(row[1]) # record the first month's profits/losses
            cur_month_val = float(row[1]) # record the first month's profits/losses as the current month
        else: # otherwise,
            last_month_val = float(row[1]) # update the last month's value as the current month's value
            prev_month_val = cur_month_val # current month becomes the previous month
            cur_month_val = float(row[1]) # the row being looked at is now the current row
        
        change = cur_month_val - prev_month_val # calculating change in profits/losses between months

        if change > greatest_inc_val: # if the change beats our greatest increase
            greatest_inc_val = change # update the value of the greatest increase
            greatest_inc_str = row[0] # update the month of the greatest increase
        elif change < greatest_dec_val: # if the change beats our greatest decrease
            greatest_dec_val = change # update the value of the greatest decrease
            greatest_dec_str = row[0] # update the month of the greatest decrease
            

        total_profits += float(row[1]) # add profits/losses to our total
        counter += 1 # increment counter by 1
    # loop ends

    # calculating average change
    avg_change = (last_month_val - first_month_val)/(counter-1)

    # rounding our numerical values
    total_profits = round(total_profits, 2)
    avg_change = round(avg_change, 2)
    greatest_inc_val = round(greatest_inc_val, 2)
    greatest_dec_val = round(greatest_dec_val, 2)

    # creating messages for our calculations
    total_months_msg = "Total Months: " + str(total_months) + '\n\n'
    total_profits_msg = "Total: $" + str(total_profits) +'\n\n'
    avg_change_msg = "Average Change: $" + str(avg_change) + '\n\n'

    greatest_inc_msg = "Greatest Increase: " + greatest_inc_str + ' ($' + str(greatest_inc_val) +')\n\n'
    greatest_dec_msg = "Greatest Decrease: " + greatest_dec_str + ' ($' + str(greatest_dec_val) + ')'

    # combining messages
    message = total_months_msg + total_profits_msg + avg_change_msg + greatest_inc_msg + greatest_dec_msg

# writing to text file
with open('./analysis/analysis.txt', 'w') as file:
    file.write(message)
print(message)
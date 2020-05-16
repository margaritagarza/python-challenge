# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
csvpath = 'Resources/budget_data.csv'

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ",")

    # use of next to skip first title row in csv file
    next(csvreader) 
    #Define the lists
    profitloss = []
    date = []
    change = []

    # Calculate lenght and total
    for row in csvreader:

        profitloss.append(float(row[1]))
        date.append(row[0])

    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months:", len(date))
    print("Total: $", int(sum(profitloss)))

 #find average, max and min
    for i in range(1,len(profitloss)):
        change.append(profitloss[i] - profitloss[i-1])   
        avg_change = sum(change)/len(change)

        max_change = max(change)

        min_change = min(change)

        max_date_location = change.index(max(change))+1
        min_date_location = change.index(min(change))+1

        max_change_date = str(date[max_date_location])
        min_change_date = str(date[min_date_location])


    print("Average Change: $", round(avg_change,2))
    print("Greatest Increase in Profits:", max_change_date,"($", int(max_change),")")
    print("Greatest Decrease in Profits:", min_change_date,"($", int(min_change),")")

with open('output.txt', "w") as f:
    f.write("Financial Analysis" + "\n")
    f.write("-----------------------------------" + "\n")
    f.write("Total Months:" + str(len(date)) + "\n")
    f.write("Total: $" + str(int(sum(profitloss))) + "\n")
    f.write("Average Change: $"+ str(round(avg_change,2)) + "\n")
    f.write("Greatest Increase in Profits:" + max_change_date +"($" + str(int(max_change)) + ")" + "\n")
    f.write("Greatest Decrease in Profits:" + min_change_date + "($" + str(int(min_change)) + ")" + "\n")



    

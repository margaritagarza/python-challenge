# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
csvpath = 'Resources/election_data.csv'

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ",")

    # use of next to skip first title row in csv file
    next(csvreader) 

    total_votes = 0
    Khan = 0
    Correy = 0
    Li = 0
    Tooley = 0

    # Calculate lenght and total
    for row in csvreader:

        if row[2] == "Khan":
            Khan= Khan + 1 
        elif row[2] == "Correy":
            Correy = Correy + 1
        elif row[2] == "Li":
            Li= Li + 1
        elif row[2] == "O'Tooley":
            Tooley = Tooley + 1
     
    #count votes   
    total_votes=Khan + Correy + Li + Tooley

    #Calculate percentages
    percentage_khan= "{:.3%}".format(Khan/ total_votes)
    percentage_correy="{:.3%}".format(Correy/ total_votes)
    percentage_li="{:.3%}".format(Li/ total_votes)
    percentage_tooley ="{:.3%}".format(Tooley/ total_votes)
    
    #Determine Winner
    list_totals= [Khan, Correy, Li, Tooley]
    if max(list_totals) == Khan:
        winner = "Khan"
    elif max(list_totals) == Correy:
        winner = "Correy"
    elif max(list_totals) == Li:
        winner = "Li"
    elif max(list_totals) == Tooley:
        winner = "O'Tooley"


    print("Election Results")
    print("-----------------------------------")
    print("Total Votes:", total_votes)
    print("-----------------------------------")
    print("Khan:", percentage_khan,"(", Khan,")")
    print("Correy:", percentage_correy,"(",Correy,")")
    print("Li:", percentage_li,"(",Li,")")
    print("O'Tooley:", percentage_tooley,"(",Tooley,")")
    print("-----------------------------------")
    print("Winner:", winner)
    print("-----------------------------------")

with open('outputpoll.txt', "w") as f:
    f.write("Election Results" + "\n")
    f.write("-----------------------------------" + "\n")
    f.write("Total Votes:" + str(total_votes) + "\n")
    f.write("-----------------------------------" + "\n")
    f.write("Khan:" + str(percentage_khan) +"("+ str(Khan)+")" + "\n")
    f.write("Correy:" + str(percentage_correy) +"("+ str(Correy) +")" + "\n")
    f.write("Li:"+ str(percentage_li) +"("+ str(Li) +")" + "\n")
    f.write("O'Tooley:"+ str(percentage_tooley) +"("+ str(Tooley) +")" + "\n")
    f.write("-----------------------------------" + "\n")
    f.write("Winner:"+ str(winner) + "\n")
    f.write("-----------------------------------" + "\n")

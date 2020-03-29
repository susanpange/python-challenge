import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

def budget_analysis(month_count, profit_count):
    total_month = len(month_count)
    total_profit = 0
    total_monthly_change = 0
    for profit in profit_count:
        total_profit += int(profit)
    
    monthly_change = []
    for i in range(len(month_count)-1):
        monthly_change_count = int(profit_count[i+1]) - int(profit_count[i])
        total_monthly_change = total_monthly_change + monthly_change_count
        monthly_change.append(monthly_change_count)
    avergae_change = round((total_monthly_change / (len(month_count) - 1)),2)

    max_change = max(monthly_change)
    min_change = min(monthly_change)
    max_change_month = month_count[monthly_change.index(max_change) + 1]
    min_change_month = month_count[monthly_change.index(min_change) + 1]


    output1 = "Financial Analysis"
    output2 = "-----------------------------------"
    output3 = "Total Months: " + str(total_month)
    output4 = "Total: $" + str(total_profit)
    output5 = "Average Change: $" + str(avergae_change)
    output6 = "Greatest Increase in Profits: " + max_change_month + " ($" + str(max_change) + ")"
    output7 = "Greatest Decrease in Profits: " + min_change_month + " ($" + str(min_change) + ")"
    output_line = [output1, output2, output3,output4, output5, output6, output7]
    for output in output_line:
        print(output)
    
    output_file = os.path.join("budget_analysis_output.csv")
    with open(output_file, "w") as datafile:
        writer = csv.writer(datafile, delimiter = "\n")

        writer.writerow(output_line)
    
    

month_count = []
profit_count = []


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)

    for row in csvreader:
        month_count.append(row[0])
        profit_count.append(row[1])
    
budget_analysis(month_count, profit_count)

output_file = os.path.join("budget_analysis_output.csv")


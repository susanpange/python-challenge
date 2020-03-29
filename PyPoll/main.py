import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

def election_analysis(vote_counting, candidate_list):
    total_votes = len(vote_counting)

    can_00_count = 0
    can_01_count = 0
    can_02_count = 0
    can_03_count = 0
    for i in range(len(vote_counting)-1):
        if vote_counting[i] == candidate_list[0]:
            can_00_count = can_00_count + 1
        if vote_counting[i] == candidate_list[1]:
            can_01_count = can_01_count + 1
        if vote_counting[i] == candidate_list[2]:
            can_02_count = can_02_count + 1
        if vote_counting[i] == candidate_list[3]:
            can_03_count = can_03_count + 1
    
    can_00_percentage = can_00_count / total_votes
    can_01_percentage = can_01_count / total_votes
    can_02_percentage = can_02_count / total_votes
    can_03_percentage = can_03_count / total_votes

    vote_count_total = [can_00_count, can_01_count, can_02_count, can_03_count]
    winner_vote_count = max(vote_count_total)
    winner = candidate_list[vote_count_total.index(winner_vote_count)]


    output1 = "Election Result"
    output2 = "-----------------------------------"
    output3 = "Total Votes: " + str(total_votes)
    output4 = "-----------------------------------"
    output5 = candidate_list[0] + " " + str('{0:.3%}'.format(can_00_percentage)) + " (" + str(can_00_count) + ")"
    output6 = candidate_list[1] + " " + str('{0:.3%}'.format(can_01_percentage)) + " (" + str(can_01_count) + ")"
    output7 = candidate_list[2] + " " + str('{0:.3%}'.format(can_02_percentage)) + " (" + str(can_02_count) + ")"
    output8 = candidate_list[3] + " " + str('{0:.3%}'.format(can_03_percentage)) + " (" + str(can_03_count) + ")"
    output9 = "-----------------------------------"
    output10 = "Winner: " + winner
    output11 = "-----------------------------------"
    output_line = [output1, output2, output3,output4, output5, output6, output7, output8, output9, output10, output11]
    for output in output_line:
        print(output)
    
    output_file = os.path.join("election_analysis_output.csv")
    with open(output_file, "w") as datafile:
        writer = csv.writer(datafile, delimiter = "\n")

        writer.writerow(output_line)
    
    
candidate_list = ["Khan", "Correy", "Li", "O'Tooley"]
vote_counting = []


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)

    for row in csvreader:
        vote_counting.append(row[2])
        
    
election_analysis(vote_counting, candidate_list)


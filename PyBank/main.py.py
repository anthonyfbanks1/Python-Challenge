#import os module 
import os
#import csv module
import csv 

#read in csv
csvpath = os.path.join('Resources', 'election_data.csv')
print(csvpath)
#make variable for total votes cast in dataset
#make variables for votes cast for each candidate in dataset
total_votes = []
stockham_votes = 0
degette_votes = 0
doane_votes = 0

#open csv for use & enter encoding (windows)
with open(csvpath,encoding="utf-8") as csvfile:
    #delimited by commas
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    #ignore headers
    csv_header = next(csvreader)
    for row in csvreader:
        #count number of votes in dataset
        total_votes.append(row[0])
        
        #count votes for each candidate
        if row[2] == "Charles Casper Stockham":
            stockham_votes +=1
        elif row[2] == "Diana DeGette":
            degette_votes +=1
        elif row[2] == "Raymon Anthony Doane": 
            doane_votes +=1

#make dictionaries out of lists to find winner
candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
candidate_votes = [stockham_votes, degette_votes, doane_votes]
#zip to pair candidates with corresponding votes and obtain the max to determine winner
votes_dict = dict(zip(candidates, candidate_votes))
winner = max(votes_dict, key=votes_dict.get)

#make a variable containing total_votes as an integer for calculations
total_vote_count = len(total_votes)
#caculate percentages of votes for each candidate
stockham_percent = (stockham_votes/total_vote_count) * 100
degette_percent = (degette_votes/total_vote_count) * 100
doane_percent = (doane_votes/total_vote_count) * 100

#print analysis to terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes : {len(total_votes)}" )
print("-------------------------")
#print percentages of votes for each candidate, rounded to 3 decimal points, and print number of votes per candidate
print(f"Charles Casper Stockham: {stockham_percent:.3f}% ({stockham_votes})")
print(f"Diana Degette: {degette_percent:.3f}% ({degette_votes})")
print(f"Raymon Anthony Doane: {doane_percent:.3f}% ({doane_votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

#export results in a text file
analysis = os.path.join("Analysis", "Election_Analysis.txt")
with open(analysis,"w") as file:

    file.write("Election Results")
    file.write("\n")
    file.write("-------------------------")
    file.write("\n")
    file.write(f"Total Votes : {len(total_votes)}" )
    file.write("\n")
    file.write("-------------------------")
    file.write("\n")
    file.write(f"Charles Casper Stockham: {stockham_percent:.3f}% ({stockham_votes})")
    file.write("\n")
    file.write(f"Diana Degette: {degette_percent:.3f}% ({degette_votes})")
    file.write("\n")
    file.write(f"Raymon Anthony Doane: {doane_percent:.3f}% ({doane_votes})")
    file.write("\n")
    file.write("-------------------------")
    file.write("\n")
    file.write(f"Winner: {winner}")
    file.write("\n")
    file.write("-------------------------")

    #Cantu, G(2018) GitHub source code [Python]. https://github.com/cantugabriela/Python-Challenge/blob/master/PyPoll/main.py
    #referenced this code to help write out text file & determine winning candidate of dataset
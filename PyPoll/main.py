# import required modules
import os
import csv

# path to the election data
csvpath = os.path.join('Resources', 'election_data.csv')

# The total number of votes cast
total_votes = 0
# A complete list of candidates who received votes
candidates = []
# The percentage and total number of votes each candidate won
count = {}
# The winner of the election based on popular vote.
x = 0
winner = ''

# open the csv report
with open(csvpath, 'r') as csvfile:

    # open a csv reader
    csvreader = csv.reader(csvfile, delimiter=',')

    # store the report header
    header = next(csvreader)

    # iterate through each row in the report
    for row in csvreader:

        # running count of total votes
        total_votes += 1

        # check if candidate voted for is included in our list yet, if not, add
        if row[2] not in candidates:
            candidates.append(row[2])

            # initialize candidate vote count
            count[row[2]] = 0
            
        # add each vote to each candidate's total
        count[row[2]] += 1

    # iterate through the final count
    for k, v in count.items():

        # check each candidate against the next for the highest count to get the winner
        if v > x:
            winner = k
            x = v

        # convert the counts for each candidate into percentages and store along with their name/count
        count[k] = [round(v/total_votes*100, 3), v]


# print the final results to terminal
print('\nElection Results')
print('---------------------------')
print('Total Votes: {}'.format(total_votes))
print('---------------------------')
for k in count:
    print('{}: {}% ({})'.format(k, count[k][0], count[k][1]))
print('---------------------------')
print('Winner: {}'.format(winner))
print('---------------------------\n')

# path to create finished report
txtpath = os.path.join('Analysis','Election_Results.txt')

# open new file to print finished report to text file
with open(txtpath, 'w') as textfile:
    textfile.write('\nElection Results\n')
    textfile.write('---------------------------\n')
    textfile.write('Total Votes: {}\n'.format(total_votes))
    textfile.write('---------------------------\n')
    for k in count:
        textfile.write('{}: {}% ({})\n'.format(k, count[k][0], count[k][1]))
    textfile.write('---------------------------\n')
    textfile.write('Winner: {}\n'.format(winner))
    textfile.write('---------------------------\n')

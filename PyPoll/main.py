import csv

with open('./Resources/election_data.csv', 'r') as file:

    data = csv.reader(file, delimiter = ',')

    votes = dict() # creating dict to hold vote counts

    # skipping and saving header row
    header = next(data)

    # iterating through data
    for row in data:
        # if the candidate is not yet found in the vote dictionary
        if row[2] not in votes.keys():
            votes.setdefault(row[2], 1) # set the initial number of votes to 1
        else:
            votes[row[2]] += 1 # otherwise, increment the vote tally by 1
    
    # total up the number of votes
    total = sum(votes.values())

    # create a dictionary to hold vote percentages
    percentages = dict()

    winner = '' # holds the name of the winning candidate
    most_votes = 0 # holds the highest number of votes

    # iterate through the candidates in the votes dictionary
    for key in votes.keys():
        # calculate the percent of the vote they got
        percentages[key] = (votes[key]/total) * 100
        percentages[key] = round(percentages[key], 3) # rounding percentages

        # if the current candidate has more votes than the previous candidates reviewed
        if votes[key] > most_votes:
            winner = key # update the name of the winning candidate
            most_votes = votes[key] # update the number of votes needed to win

# holding message to show results
results_msg = ''

# iterating through all candidates
for key in votes.keys():
    # adding candidate's results to results message
    results_msg += key + ': ' + str(percentages[key]) + "% (" + str(votes[key]) + ')\n\n'

# writing string messages for final output
title_msg = "Election Results\n\n"
delimiter = '-------------------------\n\n'
total_msg = "Total Votes: " + str(total) + '\n\n'
winner_msg = 'Winner: ' + str(winner) + '\n\n'

# combining messages
message = title_msg + delimiter + total_msg + delimiter + results_msg + delimiter + winner_msg + delimiter

# writing to text file
with open('./analysis/analysis.txt', 'w') as file:
    file.write(message)
print(message)

#add our dependencies
import csv
import os
# Create a filename variable to a direct or indirect path where the file is to be located
#file_to_save=os.path.join("analysis","election_analysis.txt")
#outfile=open(file_to_save,"w")
#outfile.write("Hello World")
#outfile.close()
#file_to_save=os.path.join("analysis","election_analysis.txt")
#with open(file_to_save, "w") as txt_file:
    #txt_file.write("Hello World")
#file_to_save=os.path.join("analysis","election_analysis_txt")
#with open(file_to_save, "w") as txt_file:
    #txt_file.write("Arapahoe\nDenver\nJefferson")
# Open the election results and read the file.

# Assign a variable to load a file from a path
file_to_load=os.path.join("Resources","election_results.csv")
# Assign a variable to save the file to a path
file_to_save=os.path.join("analysis","election_analysis.txt")

# Initialize a total vote counter.
total_votes=0

# Candidate options and candidate votes
candidate_options=[]
candidate_votes={}
# Create variable for winning candidate, vote count, and percentage
winning_candidate = ""
winning_count= 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data)


    # Read  the header row.
    headers=next(file_reader)
    
    # Print each row in the CSV File
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name]=0

         # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

    # Save the results to our text file
    with open(file_to_save, "w") as txt_file:

        election_results =(
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
        print(election_results, end="")
    # Save the final vote count to the text file.
        txt_file.write(election_results)

        for candidate_name in candidate_votes:
        # Retrieve vote count and percentage
            votes = candidate_votes[candidate_name]
            vote_percentage = float(votes) / float(total_votes) * 100
            candidate_results =(
                f"{candidate_name}:  {vote_percentage:.1f}% ({votes:,})\n")
            
        # Print each candidate, their voter count, and percentage to the terminal
            print(candidate_results)

        # Save the candidate results to our text file.
            txt_file.write(candidate_results)

        
        # Determine winning vote count, winning percentage, and candidate
            if (votes > winning_count) and (vote_percentage  > winning_percentage):
                winning_count = votes
                winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
                winning_candidate = candidate_name


        
    #Print the winning candidate's results to the terminal
    winning_candidate_summary = (
            f"-----------------------\n" 
            f"Winner:{winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"------------------------\n")

    print(winning_candidate_summary)




    # Save the winning candidate's results to the text file.


    





            

    # Determine the percentage of votes for each candidate by looping through candidate list and options
    # Iterate through the candidate list.
    #for candidate_name in candidate_votes:
        # Retrieve the vote count of a candidate.
        #votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        #vote_percentage = float(votes) / float(total_votes) * 100
        
        # Print each candidate name, vote count and percentage of # votes to the terminal
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")







    # To do: print out the winning candidate, vote count and percentage. 
    #print(f"{candidate_name}: received {vote_percentage}% of the vote.")



# Print the candidate vote dictionary.
#print(candidate_votes)


# Print the candidate list. 
#print(candidate_options)


# 3. Print the total votes
    #print(total_votes)








































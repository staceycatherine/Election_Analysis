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

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data)
    # Print each row in the CS file.
    #for row in file_reader:
       # print(row)

     # Read and print the header row.
    headers=next(file_reader)
    print(headers)
    
























#file_to_save=os.path.join("analysis","election_analysis.txt")











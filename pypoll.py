#!/usr/bin/env python
# coding: utf-8

# In[6]:


import csv
import os

file_to_load = os.path.join(".","Resources","election_data.csv")
file_to_output = os.path.join(".","election_anaylisis.txt")
candidate =[]
total_votes = 0
candidate_votes ={}
candidate_options = []
winning_candidate=""
winning_count = 0

with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    header = next(reader)
    
    for row in reader:
        total_votes = total_votes + 1

    candidate_name = row[2]

    if candidate_name not in candidate_options:
        candidate_options.append(candidate_name)
        candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1

    print(candidate_votes)
    print(candidate_options)
    with open(file_to_output, "w") as txt_file:
        election_results =(
    f"Election Results\n"
    f"--------------------\n"
    f"Total Votes {total_votes}\n"
    f"--------------------\n"
    
)
    

    print(election_results, end="")

    for candidate in candidate_votes:
       votes = candidate_votes[candidate]
    vote_percentage = float(total_votes) /float (votes)*100

    if(total_votes > winning_count):
        winning_count = votes
        winning_candidate = candidate

        if(total_votes>winning_count):
            Winning_count = votes
            winning_candidate = candidate

        voter_output = f"{candidate}: {vote_percentage:.3f}%({votes})\n"
    
   
    print(voter_output,end="")
 
    winning_candidate_summary=(
        f"-----------------------\n"
        f"Winner:{winning_candidate}\n"
        f"-----------------------\n"
    )
print(winning_candidate_summary)



# In[ ]:





# In[ ]:





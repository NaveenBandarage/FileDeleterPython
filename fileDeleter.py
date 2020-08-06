import os
from os import listdir
import sys

#directory that we are going into to delete stuff 
#change this to whatever directory you need 
directory = "/Users/naveenbandarage/Documents/Screenshots"

files_in_directory = os.listdir(directory) #stores directory 
filtered_files = [file for file in files_in_directory if file.startswith("Screen Shot")] #looks through all the files that start with Screenshot.
for file in filtered_files: 
	path_to_file = os.path.join(directory, file) #for each loop that deletes them 
	os.remove(path_to_file)


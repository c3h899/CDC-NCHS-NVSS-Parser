import pandas as pd
from Table_Rules import Fetal_2020

# Import Rules from Table_Rules (Mostly for Clean Code)
Fetal_2020_CDC = Fetal_2020()

# Simple Function to Implement the Substring Access
# Python does not seem to be very verbose in string safety requirements
# Use of external function is to easibly accomodate future changes
def SubString(Str_Ref, Start, Stop):
	Str = Str_Ref[(Start - 1):Stop].strip()
	return Str if Str is not None else ""

# Principle Parser
# Iterates through list of rules and returns a fixed-length list of responses
# Categories whose value are none are reported as such.
def ParseLine(Str_Ref, Rules):
	Record = list() # Initialize new List
	for key, start, stop in Rules:
		entry_value = SubString(Str_Ref, start, stop)
		Record.append(entry_value)
	return Record

# Principle Code
# Takes File by Name, and Applies Rules
# Returns Formatted Data
def ReadFile(FName, Rules):
	Rules.sort(key = lambda x: x[1])
	# Sort the Rules by Start (Value of the Integer in Position 2)
	# This Allows the data to be accessed in a (mostly) Monotonic order
	# https://www.geeksforgeeks.org/python-program-to-sort-a-list-of-tuples-by-second-item/
	Results = list()
	# Iterate Through File
	# https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/
	ii = 0
	Result = list()
	with open(FName) as file:
		Lines = file.readlines()
		for line in Lines:
			if line != '\n':
				result = ParseLine(line, Rules)
				if result is not None: Results.append(result)
	# Extract Column Headers
	Columns = list()
	for key, start, stop in Rules:
		Columns.append(key)
	# Convert List of List to Table
	df = pd.DataFrame(Results, columns = Columns)
	return df

# MAIN CODE
fname = 'Fetal2020US_COD.txt'
Table = ReadFile(fname, Fetal_2020_CDC)
Table.to_csv(f"{fname[:-4]}.csv", index=False)

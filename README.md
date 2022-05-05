7z File Contains Input Text (Extract Before Running)
CSV Is Formatted Output
Parse.py Utility

Code is barebones and inelegant.

User can customize and define rulesets for parsing using the formate specified in lines 3...8:

- Basic Formatting, List of Data Elements and Locations
- Input is based on specified values in https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/DVS/fetaldeath/2020fetaluserguide.pdf
- Rules are specified as an (unsorted) list of tuples, each tuple consists of 3 values
- 1 (String) Data Item Label (Use Colons to Denote Sub-Categories, Use NO SPACES)
- 2 (Integer) Location Start
- 3 (Integer) Location Stop (End of Range, or Repeat Start Location if Not Specified)

File is read and rules are applied

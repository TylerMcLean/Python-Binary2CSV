# Python-Binary2CSV
Binary to CSV - Python Script for converting Binary files to CSV

A simple but useful utility that I used to reverse-engineer some generic data files. The output can be graphed in Excel to search for patterns.
Developed and tested in Python 3.

Specify Input and Output files and delimiting options at the start of the script.

## Example:

###### input.dat (when viewed with a tool such as HxD)
```
07 3B 02 71 ED F1 F2 0F 09 0D 08 00 02 61 ED F1 F2 0F 09 0D 08 01 02 58 ED D9 DA 0F 09 0D 07 39 15 00 ED E9 EA 0F 09 0D
```

Settings:
```
input = "input.dat"
output = "output.csv"
delim = 1
newline = 10
```

###### output.csv
```
7,59,2,113,237,241,242,15,9,13,
8,0,2,97,237,241,242,15,9,13,
8,1,2,88,237,217,218,15,9,13,
7,57,21,0,237,233,234,15,9,13
```

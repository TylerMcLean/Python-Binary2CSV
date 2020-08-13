input = "input.dat"                                                             # Input File
output = "output.csv"                                                           # Output File:

delim = 1                                                                       # Insert separator every n bytes
newline = 10                                                                    # Insert newline every n delimiters

# -------------------

delim = delim * 2                                                               # Bytes in hex are 2 characters long

f=open(input,"rb")
o=open(output,"w")

content=f.read().hex()                                                          # Read file as hex bytes
content=','.join(content[i:i+delim] for i in range(0, len(content), delim))     # Insert Delimiters
content=content.split(',')                                                      # Split into array

cLength = len(content)

for x in range(cLength):                                                        # Convert to Decimal
  content[x] = int(content[x],16)

for x in range(cLength):                                                        # Insert NewLines
  if not (x)%newline and x>0:
    content[x] = "\n" + str(content[x])

content = listToStr = ','.join(map(str, content))                               # Convert to string
content = content.replace(",\n", "\n")                                          # Remove Trailing Commas

o.write(content)
o.close()
f.close()

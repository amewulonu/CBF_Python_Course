
file = open("cbf.txt", "r")
for line in file:
    stripped_line = line.strip()
    print(stripped_line)
file.close()    

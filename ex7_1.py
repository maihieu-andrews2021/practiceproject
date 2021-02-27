fh = open('mbox-short.txt')
count = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith ('From '):
        continue
    spt = line.split()
    count = count +1
    print(spt[1])
print("There were", count, "lines in the file with From as the first word")


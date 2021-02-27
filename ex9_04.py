#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
fh = open('mbox-short.txt')
counts = dict()
lst = list()
hicount=None
hiperson=None
for line in fh:
    line = line.rstrip()
    if not line.startswith ('From '):
        continue
    spt = line.split()
    email= spt[1]
    lst.append(email)
for person in lst:
    counts[person]=counts.get(person,0) +1
for person,num in counts.items():
    if hicount is None or num > hicount:
        hiperson=person
        hicount = num
print(hiperson, hicount)




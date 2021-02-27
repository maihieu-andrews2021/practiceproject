#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
fh=open('mbox-short.txt')
lst=list()
hrlst=list()
count = 0
hours=dict()
for line in fh: 
    line = line.rstrip()
    if not line.startswith('From'):
        continue   
    #print('Line:', line)
    lst=line.split()
    #print('List:', lst)
    #guardian for time line
    if len(lst) < 5:
        continue
    time=lst[5]
    #print('Time:', time)
    spthr=time.split(':')
    hrs=spthr[0]
    hrlst.append(hrs)
hrlst.sort()
for hr in hrlst:
    hours[hr]=hours.get(hr,0) + 1
for hour,cnt in hours.items():
    print(hour,cnt)



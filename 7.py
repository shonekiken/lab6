file=open ("mailbox.txt","r")
fout=open("output.txt","w")
dates=[]
for line in file:
    if line.startswith("Date:"):
        date=line.split(":")[1].strip()
        date=" ".join(date.split()[:3])
        if date not in dates:
            dates.append(date)
for date in sorted(dates):
    fout.write(date +"\n")
file.close()
fout.close()

file=open ("mailbox.txt","r")
fout=open("output.txt","w")
domains=[]
lines=file.readlines()
for line in lines:
    if line.startswith("From:"):
        dom=line.split("@")[1]
        if dom not in domains:
            domains.append(dom)
for dom in sorted(domains):
    fout.write(dom+"\n")
file.close()
fout.close()

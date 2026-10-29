file=open('mailbox.txt','r')
fout=open('output.txt','w')

java_list = []
count = 0
for line in file:
    if 'java' in line:
        count += 1
        java_list.append(line)

fout.write(str(count))
file.close()
fout.close()


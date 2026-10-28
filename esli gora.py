numbers = []
with open("mailbox.txt","r") as file:
    for line in file:
        if "with ESMTP id" in line:
            number =line.split("with ESMTP id")[1].split(";")[0].strip()
            numbers.append(number)
numbers=list(set(numbers))
numbers.sort()

with open("output.txt","w") as file:
    for number in numbers:
        file.write(number+"\n")

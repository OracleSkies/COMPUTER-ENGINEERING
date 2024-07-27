array = ["J","J","J","J"]
end = []
counts = {""}
array = {"J":0,"J1":0,"J2":0,"J3":0}

'''for letter in array:
    hold = letter
    count = end.count(hold)
    if hold not in end:
        end.append(hold)
    else:
        while hold in end:
            count += 1
        end.append(hold + str(count))

count = array.count("J")

for i in range(1,5):
    count += 1

print(end)'''


for letter in array:
    count = counts.get(letter,0)
    if count == 0:
        end.append(letter)
    else:
        end.append(letter + str(count))
    counts[letter] = count+1
print(end)
file = open('day8.txt', 'r')
lines = file.readlines()
count = 0
for line in lines:
    split1 = line.split(' | ')
    output1 = split1[1]
    output = output1.split(" ")
    output[-1] = output[-1].strip('\n')
    for i in range(0, len(output)):
        if(len(output[i]) == 2 or len(output[i]) == 3 or len(output[i]) == 4 or len(output[i]) == 7):
           count += 1

print(count)

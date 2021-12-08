file = open('day8.txt', 'r')
lines = file.readlines()
count = 0
for line in lines:
    split1 = line.split(' | ')
    output1 = split1[1]
    output = output1.split(" ")
    output[-1] = output[-1].strip('\n')
    sixes = []
    fives = []
    signals1 = split1[0]
    signals = signals1.split(" ")
    for i in range(0, len(signals)):
        if len(signals[i]) == 2:
            onea = sorted(signals[i])
            one = "".join(onea)
        elif len(signals[i]) == 3:
            sevena = sorted(signals[i])
            seven = "".join(sevena)
        elif len(signals[i]) == 4:
            foura = sorted(signals[i])
            four = "".join(foura)
        elif len(signals[i]) == 7:
            eighta = sorted(signals[i])
            eight = "".join(eighta)
        elif len(signals[i]) == 6:
            sixes.append(signals[i])
        elif len(signals[i]) == 5:
            fives.append(signals[i])
    for x in range(0, len(fives)):
        if one[0] in fives[x] and one[1] in fives[x]:
            threea = sorted(fives[x])
            three = "".join(threea)
            del fives[x]
            break
    for y in range(0, len(sixes)):
        if three[0] in sixes[y] and three[1] in sixes[y] and three[2] in sixes[y] and three[3] in sixes[y] and three[4] in sixes[y]:
            ninea = sorted(sixes[y])
            nine = "".join(ninea)
            del sixes[y]
            break
    if one[0] in sixes[0] and one[1] in sixes[0]:
        zeroa = sorted(sixes[0])
        sixa = sorted(sixes[1])
        zero = "".join(zeroa)
        six = "".join(sixa)
    else:
        zeroa = sorted(sixes[1])
        sixa = sorted(sixes[0])
        zero = "".join(zeroa)
        six = "".join(sixa)
        
    if "a" in eight and not("a" in three) and not("a" in four):
        mystery = "a"
    elif "b" in eight and not("b" in three) and not("b" in four):
        mystery = "b"
    elif "c" in eight and not("c" in three) and not("c" in four):
        mystery = "c"
    elif "d" in eight and not("d" in three) and not("d" in four):
        mystery = "d"
    elif "e" in eight and not("e" in three) and not("e" in four):
        mystery = "e"
    elif "f" in eight and not("f" in three) and not("f" in four):
        mystery = "f"
    elif "g" in eight and not("g" in three) and not("g" in four):
        mystery = "g"
    if mystery in fives[0]:
        twoa = sorted(fives[0])
        fivea = sorted(fives[1])
        two = "".join(twoa)
        five = "".join(fivea)
    else:
        twoa = sorted(fives[1])
        fivea = sorted(fives[0])
        two = "".join(twoa)
        five = "".join(fivea)
    total = [zero, one, two, three, four, five, six, seven, eight, nine]
    outputa = sorted(output[0])
    outputb = sorted(output[1])
    outputc = sorted(output[2])
    outputd = sorted(output[3])
    output[0] = "".join(outputa)
    output[1] = "".join(outputb)
    output[2] = "".join(outputc)
    output[3] = "".join(outputd)
    for a in range(0, len(total)):
        if output[0] == total[a]:
            output1 = str(a)
            break
    for b in range(0, len(total)):
        if output[1] == total[b]:
            output2 = str(b)
            break
    for c in range(0, len(total)):
        if output[2] == total[c]:
            output3 = str(c)
            break
    for d in range(0, len(total)):
        if output[3] == total[d]:
            output4 = str(d)
            break
    finaloutput = output1 + output2 + output3 + output4
    finaloutput = int(finaloutput)
    count += finaloutput
print(count)

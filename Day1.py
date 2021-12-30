with open("input.txt") as file:
    lines = file.readlines()
    lines = [int(line.rstrip()) for line in lines]
    x = 0
    for i in range(1,len(lines)-2):
        if i>=3 and  lines[i:i+3] > lines[i:i+2]:
            x+=1
print(x)




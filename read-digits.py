with open("bit-map.txt", 'r') as file:
    all_file = file.read().strip()
    all_file_list = all_file.split('\n')
    lines = [[int(each_int) for each_int in line.split()] for line in all_file_list]

def trace(i, j, lines):
    isDone = False

    while (not isDone):
        lines[i][j] = -1
        if lines[i][j+1] == 0:
            j += 1
            continue
        if lines[i+1][j] == 0:
            i += 1
            continue
        if lines[i][j-1] == 0:
            j -= 1
            continue
        if lines[i-1][j] == 0:
            i -= 1
            continue
        isDone = True

count = 0
z = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == z:
            print('ENTER')
            count += 1
            trace(i, j, lines)
            continue

print(count)



   

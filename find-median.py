from queue import Queue

q = Queue(maxsize = 8)

q.put(4)
q.put(7)
q.put(20)
q.put(1)
q.put(13)
q.put(11)
q.put(18)
q.put(12)
n = q.qsize()

smallest = 1000
for i in range(n):
    temp = q.get()
    if smallest > temp:
        smallest = temp
    q.put(temp)
count = 1

if n % 2 == 0:
    med1 = int(n/2)-1
    med2 = int(n/2)
    val1 = 0
    val2 = 0

    for i in range(med2 + 1):
        tempSmallest = 1000
        for j in range(n):
            temp = q.get()
            if temp <= smallest:
                q.put(temp)
                continue
            if tempSmallest > temp:
                tempSmallest = temp
            q.put(temp)
        smallest = tempSmallest
        if count == med1:
            val1 = smallest
        if count == med2:
            val2 = smallest
            break
        count += 1
    print((val1 + val2)/2)
else:
    med = int(n/2)
    val = 0
    for i in range(med + 1):
        tempSmallest = 1000
        for j in range(n):
            temp = q.get()
            if temp <= smallest:
                q.put(temp)
                continue
            if tempSmallest > temp:
                tempSmallest = temp
            q.put(temp)
        smallest = tempSmallest
        if count == med:
            val = smallest
            break
        count += 1
    print(val)

for i in list(q.queue):
    print(i, end=" ")
print()

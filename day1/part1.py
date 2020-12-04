# use vim regex ":%s/\n/,/g", add [ and ] at beginning and end

f = open("input","r")

arr = []
b = False

for line in f.readlines():
    arr += [int(line.rstrip("\n"))]

length = len(arr)

for i in range(0,length):
    for j in range(0,length):
        if (arr[i]+arr[j] == 2020):
            print("Result = ", (arr[i]*arr[j]))
            b = True
    if (b):
        break

f.close()

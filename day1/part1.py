# use vim regex ":%s/\n/,/g", add [ and ] at beginning and end

arr = []

with open("input","r") as f:
    for i in f.readlines():
            arr = arr + [int(i.rstrip("\n"))]

b = False


length = len(arr)


for i in range(0,length):
    for j in range(0,length):
        if (arr[i]+arr[j] == 2020):
            print("Result = ", (arr[i]*arr[j]))
            b = True
    if (b):
        break

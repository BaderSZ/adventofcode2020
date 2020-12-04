
f = open("input","r")

arr = []
b = False

for line in f.readlines():
    arr += [int(line.rstrip("\n"))]

length = len(arr)

for i in range(0,length):
    for j in range(0,length):
        for k in range(0,length):
            if (arr[i]+arr[j]+arr[k] == 2020):
                print("Result = ", arr[i]*arr[j]*arr[k])
                b = True
        if (b):
            break

f.close()

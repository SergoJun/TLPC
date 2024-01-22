lenght_1 = 10001
lenght_2 = 10001
while (lenght_1 > 10000):
    print("first (L1) tongue length (<=10000)")
    lenght_1 = int(input())
while (lenght_2 > 10000):
    print("second (L2) tongue length (<=10000)")
    lenght_2 = int(input())
k=0
L1 = []
L2 = []
L = []
while (lenght_1 != k):
    print("enter the content of the chain for L1 (<=100)")
    h = str(input())
    if len(h) <= 100:
        L1.append(h)
        k = k+1
    else:
        print("error")
k=0
while (lenght_2 != k):
    print("enter the content of the chain for L2 (<=100)")
    h = str(input())
    if len(h) <= 100:
        L2.append(h)
        k = k+1
    else:
        print("error")
for i in L1:
    for j in L2:
        L.append(i+j)
print("L1=",L1)
print("L2=",L2)
print("L=",L)
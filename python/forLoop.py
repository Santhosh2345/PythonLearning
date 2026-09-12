for i in range(1, 11):
    print (i, end=" ")
print()

for i in range(1, 21):
    if i % 2 == 0:
        print (i, end=" ")
print()

for i in "Santhosh Kumar P":
    print(i)
print()

for i in range (0, 4):
    for j in range (i+1):
        print("*", end=" ")
    print()
print()

for i in [200, 404, 500, 301, 403]:
    if(i == 200):
        print("OK")
    else:
        print(i)

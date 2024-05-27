
# 长方形
i=1
while(i<=3):
    print("*"*4)
    i=i+1

print()

i=1
while(i<=5):
    print("*"*i)
    i=i+1

print()

i=5
while(i>=0):
    print("*" * i)
    i=i-1

print()

n = 5
i = 0
while i < n:
    spaces = n - i - 1
    while spaces > 0:
        print(" ", end="")
        spaces -= 1
    stars = 2 * i + 1
    while stars > 0:
        print("*", end="")
        stars =stars-1
    print()
    i += 1

print()

# 菱形
n = 5
i = 0
while i < n:
    spaces = n - i - 1
    while spaces > 0:
        print(" ", end="")
        spaces -= 1
    stars = 2 * i + 1
    while stars > 0:
        print("*", end="")
        stars -= 1
    print()
    i += 1
i = n - 2
while i >= 0:
    spaces = n - i - 1
    while spaces > 0:
        print(" ", end="")
        spaces -= 1
    stars = 2 * i + 1
    while stars > 0:
        print("*", end="")
        stars -= 1
    print()
    i -= 1

print()

# 中空菱形
for i in  range(6):
    if(i==1):
        print(" "*2+"*"+" "*2)
    if(i==2):
        print(" "+"*"+" "+"*"+" ")
    if(i==3):
        print("*"+"   "+"*")
    if(i==4):
        print(" "+"*"+" "+"*"+" ")
    if(i==5):
        print(" " * 2 + "*" + " " * 2)

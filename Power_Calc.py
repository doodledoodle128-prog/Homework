base = int(input("Enter the base: "))
expo = int(input("Enter the exponent: "))

ans = 1

for i in range(expo):
    ans = base * ans
print("the answer is",ans)
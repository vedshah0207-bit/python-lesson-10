lower = int(input("Enter the minimum number of the prime numbers you want to find. "))
higher = int(input("Enter the maximum number of the prime numbers you want to find. "))

print("Prime numbers between", lower, "and", higher, "are")

for num in range(lower, higher + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
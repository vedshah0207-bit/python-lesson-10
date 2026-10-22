num = int(input("Enter a number please. "))
t = num
num_len = 0

while t > 0:
    num_len += 1
    t = int(t / 10)

if num_len >= 4:
    num_len = int(num_len / 2)
    chk = 0

    while num > 0:
        rem = num % 10

        if chk == num_len:
            mid_1 = rem
        elif chk == (num_len - 1):
            mid_2 = rem
        num = int(num / 10)
        chk += 1
    prod = mid_1 * mid_2
    print("The product of the mid-digits is", prod)
else:
    print("ERROR your number is less than 4 numbers")

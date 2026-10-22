string = input("Enter a word please. ")
char = input("Please enter the character you want to find. ")
i = 0
count = 0

while (i < len(string)):   #this will check if i (letter we're on) is smaller the lenghts of the string otherwise we would keep checking forever
    if (string[i] == char): #string[i] means that i is basically the leteer we are on and it will the the 'i' letter that we are on then compare it to char
        count += 1

    i +=1
print("The total number of times", char, "appears is", count, "times")
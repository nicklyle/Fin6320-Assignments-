import random 

count = 0

print("Lets see what your fortune is today! hmm looks like")

while count < 1:
    
    fortune = random.randint(1,5)
    
    if fortune == 1:
        print("Nick Lyle will receive extra credit in the future")
        count += 1
    elif fortune == 2:
        print("someone with the initials NL will be given an A on the midterm")
        count += 1 
    elif fortune == 3:
        print("everyone will recieve 10 extra credit points on their midterm")
        count += 1
    elif fortune == 4:
        print("the word of the day is orthogonal, no fortune for you!")
        count += 1
    elif fortune == 5:
        print("sorry no fortune today, goodluck!")
        count +=1 


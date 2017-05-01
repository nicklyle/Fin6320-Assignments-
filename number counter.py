 

print("I am going to count between two numbers you provide me")
print("Please enter a lower bound")
lower = int(input())
print("Please enter an upper bound")
upper = int(input())
count = int(lower)
print("please enter a number by which to count.")
factor = int(input())

while count < upper:
    
    if count < upper:
        count += factor
        print(count)
        
    elif count > upper:
        break
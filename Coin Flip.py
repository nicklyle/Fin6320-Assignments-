import random 

count = 0 

tails = 0
heads = 0 

while count < 100:
    
    outcome = random.randint(1,2)
    
    if outcome == 1:
        print("Tails")
        tails += 1
        count += 1
    elif outcome == 2:
        print("Heads")
        heads += 1
        count += 1 
print("You flipped heads a total of", heads , "and you flipped tails", tails , "times") 
        
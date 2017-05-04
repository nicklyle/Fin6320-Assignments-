import random

words = ["Money", "Finance", "Economics", "Hedging", "Derivatives", "Austrian"]

for i in range (len(words)):
    random_index = random.randrange(len(words))
    print (words[random_index])
    del words[random_index]
    

#guess_word game

words = ("Finance",
         "Economics",
         "Money",
         "Austrian",
         "Hedging")

choice = int(input("Enter a number from 1 to 5: "))
print("Take a guess, word has",len(words[choice]),"letters:")
print(words[choice])
guess = input("Take a guess: ")
tries = 0
letter = ""

while guess != words[choice]:
    print("\nKeep trying!")
    if tries != 5:
        letter_question = input("Want to ask for a letter yes/no? ")
        if letter_question == "yes" or letter_question == "y":
            letter_guess = input("Enter a letter: ")
            if letter_guess in words[choice]:
                print(letter_guess, "is in word")
                tries += 1            
                guess = input("Take a guess: ")
          
            else:
                print("Letter not in word")
                tries += 1
                guess = input("->>Take a guess: ")
                if guess == words[choice]:
                    print("You guessed the word")
                    break
                else:
                    continue
        else:
            continue
    else:
        print("You lose, sorry!")
        break


print("See you soon!")
            

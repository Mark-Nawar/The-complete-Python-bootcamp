import random
def hangman():
    word = random.choice(["mark", "pen","lion","corona","jesus","life","avengers","the"])
    turns=10
    guessmade= ''

    while (true):
        main = ""
        missed =0
        # here don't worry about the spaces because for every loop if the guess is true the space is replaced by the letter.
        for letter in word:
            if letter in word:
                main =main +letter
            else:
                main = main + "_"+" "
            if main == word:
                print(main+ "is the right word good job you saved the man")
                break
            print("guess the word : "+main )
            guess= input().lower()
            if guess.isalpha():
                guessmade += guess
            else:
                print("Enter only alpha characters ")
            if guess not in word:
                turns-=1
                if turns ==9:
                    print("9 turns left")
                    print("  --------  ")
                if turns == 8:
                    print("8 turns left")
                    print("  --------  ")
                    print("     O      ")
                if turns == 7:
                    print("7 turns left")
                    print("  --------  ")
                    print("     O      ")
                    print("     |      ")
                if turns == 6:
                    print("6 turns left")
                    print("  --------  ")
                    print("     O      ")
                    print("     |      ")
                    print("    /       ")
                if turns == 5:
                    print("5 turns left")
                    print("  --------  ")
                    print("     O      ")
                    print("     |      ")
                    print("    / \     ")
                if turns == 4:
                    print("4 turns left")
                    print("  --------  ")
                    print("   \ O      ")
                    print("     |      ")
                    print("    / \     ")
                if turns == 3:
                    print("3 turns left")
                    print("  --------  ")
                    print("   \ O /    ")
                    print("     |      ")
                    print("    / \     ")
                if turns == 2:
                    print("2 turns left")
                    print("  --------  ")
                    print("   \ O /|   ")
                    print("     |      ")
                    print("    / \     ")
                if turns == 1:
                    print("1 turns left")
                    print("Last breaths counting, Take care!")
                    print("  --------  ")
                    print("   \ O_|/   ")
                    print("     |      ")
                    print("    / \     ")
                if turns == 0:
                    print("You loose")
                    print("You let a kind man die")
                    print("  --------  ")
                    print("     O_|    ")
                    print("    /|\      ")
                    print("    / \     ")
                    break
name=input("enter your name plz")
print("hello welcome to the hangman game ")
hangman()
print()

def hangman(word):
    
    try:
        word = word.lower()
        wrong = 0

        stages = ["",
                  "_______        ",
                  "|      |       ",
                  "|      0       ",
                  "|     /|\      ",
                  "|     / \      ",
                  "|______________"]
        
        rletters = list(word)

        board = ["_"] * len(word)

        win = False

        print("Welcome to Hangman!!!")


        while wrong < len(stages) - 1:

            print("\n")

            msg = "Guess a letter, fool"

            char = input(msg)

            if char in rletters:

                cind = rletters.index(char)

                board[cind] = char

                rletters[cind] = "$"
            else:
                wrong += 1
            
            print((" ".join(board)))

            e = wrong + 1

            print("\n".join(stages[0 : e]))

            if "_" not in board:
                print("You win!")

                print(" ".join(board))

                win = True

                break
        if not win:
            
            print("You fuckin lose, ya goob. The answer was obviously FART. Just kidding! The real answer was {}.".format(word.upper())) 
    except AttributeError:
        print("How about you write a proper fucking word you absolute dogshit of a person you clown")

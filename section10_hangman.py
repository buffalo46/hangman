def hangman(word):
    wrong = 0 #count how many mistakes
    stages = ["",
              "_________    ",
              "|            ",
              "|    |       ",
              "|    0       ",
              "|   /|\      ",
              "|   / \      ",
              "|            "
              ]
    rletters = list(word) #convert word in list
    board = ["_"] * len(word) #list to show hint
    win = False
    print("welcome to hangman")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "guess one letter: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char) #where it is?
            board[cind] = char #change 'board' from "_" to the letter
            rletters[cind] = '$' #make the lettter non alphabet
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e])) # show hangman
        if "_" not in board:
            print("you win!")
            print(" ".join(board))
            win = True
            break
    
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("you lose! answer is {}.".format(word))

import random
answer = ["cat", "dog", "hat"]
random_number = random.randint(0, 2)
word = answer[random_number]

hangman(word)





#Pong2 Launcher

import Pong2 as p2
import sys, webbrowser

choose = None
while choose != "6":
    print(
    """
_Menu Pong2_
    by BartekBanas
__________________
1.Play
2.Show scores
3.Reset the scores
4.Source
5.About game
6.Exit
__________________
""")

    choose=input("Your choose:")

    if choose=="1":
        p2.game()
        print("Thanks for game")
        sys.exit()
    
    elif choose=="2":
        try:
            score=open("score.txt","r")
            lines=score.readlines()
            print("\nScores:\n")
            for line in lines:
                print(line)
        except IOError as e:
            print("Sorry, this file does not exist.", e)
            input("Enter.")

    elif choose=="3":
            blank=""
            score=open("score.txt","w")
            score.write(blank)
            print("Done!")

    elif choose=="4":
        pyweb="https://www.python.org/"
        pygame="https://www.pygame.org/news"
        pyLW="https://github.com/livewires/python"
        print("Source: \n")
        print(pyweb)
        print("-------------------------------------")
        print(pygame)
        print("-------------------------------------")
        print(pyLW)
        print("-------------------------------------")
        ask=input("Do you want open this websites?(y/n)")
        print(ask)
        if ask.lower()=="y":
            webbrowser.open(pyweb)
            webbrowser.open(pygame)
            webbrowser.open(pyLW)
        else:
            None

    elif choose=="5":
        print(
            """
Pong2 is my version of the classic
Pong game. In spite of the lack of
certain elements, the game accurately
reproduces the original. To win you
need to score 8 points.
Bartek Banaś
11/18/2017
"""
            )
    elif choose=="6":
        print("BAY!")


    else:
        print("\nSorry. This option does not exist")
        

    
    

# JTSK-350112
# a6_1.py
# Wossen Hailemariam
# w.hailemariam@jacobs-university.de


import random
#
#class Rqballgame():
#
#    def __init__(self,playerone_name, playertwo_name, numberof_games):
#        self._playerone_name = playerone_name
#        self._playertwo_name = playertwo_name
#        self._numberof_games = numberof_games
#        self.plone_score = 0
#        self.pltwo_score = 0
#
#    def getplone_score(self):
#     
#        probability = 0.5
#        for i in range(number_rounds):
#            if random() >= probability:
#                self.plone_score = self.score + 1
#        return self.score
#
#    def getpltwo_core(self):
#
#        probability = 0.5
#        for i in range(number_rounds):
#            if random() >= probability:
#                self.pltwo_score = self.score + 1
#        return self.pltwo_score
#           
#def compare():
#    if Rqballgame.getplone_score > Rqballgame.getplone_score:
#        print ('Player One has WON')
#    elif Rqballgame.getplone_score < Rqbvallgame.getpltwo_score:
#        print ('Player Two has WON')
#    else:
#        print("It's a Draw")
#        

    from itertools import cycle

def printIntro():
    print('Racquetball Simulation')
    print('Direction:\n\
        \t-Input Players\n\
        \t-Input the Number of Games')
def alternate(A,B):
    myIterator = cycle(range(2))

    x = myIterator.next()   # or next(myIterator) which works in Python 3.x. Yields 0
    x = myIterator.next()   # or next(myIterator) which works in Python 3.x. Yields 1
    # etc.
    if x == False:
        return B
    else:
        return A


def simNGames(probA, probB, n):
    winsA = 0
    winsB = 0
    thisdict = {
        prob = 
        score =
        wins =


    }
    for i in range(n):
        if random() >= probA:
            winsA = winsA + 1
        elif random() >= probB:
            winsB = winsB + 1
    return winsA, winsB



def printSummary(winA, winB):
    print('The score of the Fisrt player is:', winA)
    print('The score of the Second Player  is:', winA)


def main():
    printIntro()
    A = float(input())
    B = float(input())
    n = int(input())
    winsA, winsB = simNGames(A,B,n)

    printSummary(winsA,winsB)

main()
 

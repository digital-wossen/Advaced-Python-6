
import random


def printIntro():
    print('Racquetball Simulation')
    print('Direction:\n\
        \t-Input Players\n\
        \t-Input the Number of Games')
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

def simNGames(probA, probB, n):
    #winsA, winsB = 0
    for i in range(n):
        if random() > probA:
            winsA = winsA + 1
        elif random() > probB:
            winsB = winsB + 1
    return winsA, winsB
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



def printSummary(winA, winB):
    print('The score of the Fisrt player is:', winA)
    print('The score of the Second Player  is:', winA)


def main():
    printIntro()
    A = float(input())
    B = float(input())
    n = int(input())
    winsA, winsB = simNGames(A,B,n)
#           
#def compare():
#    if Rqballgame.getplone_score > Rqballgame.getplone_score:
#        print ('Player One has WON')
#    elif Rqballgame.getplone_score < Rqbvallgame.getpltwo_score:
#        print ('Player Two has WON')
#    else:
#        print("It's a Draw")
    printSummary(winsA,winsB)

main()
 
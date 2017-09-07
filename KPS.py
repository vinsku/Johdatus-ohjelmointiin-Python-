#KPS.py
#Pelaaja1 ja pelaaja2
#Pelaaja 1 voittaa, pelaaja 2 häviää // Pelaaja2 voittaa, pelaaja1 häviää
#Kivi voittaa: sakset - sakset voittaa: paperin - paperi voittaa: kiven
def main():

    def play_game(player1, player2, beats):

        if (player1 == player2):
         return ("It's a tie!")
        elif (player1 == beats[player2]):
            return ("Player 1 won!")
        elif (player2 == beats[player1]):
            return ("Player 2 won!")

    beats = {
        'S': 'R',
        'R': 'P',
        'P': 'S',
         }


    player1 = input("Player 1, enter your choice (R/P/S): ")
    while player1 not in beats.keys():
        player1 = input("That isn't an option. Please try again.")

    player2 = input("Player 2, enter your choice (R/P/S): ")
    while player2 not in beats.keys():
        player2 = input("That isn't an option. Please try again.")

    if (player1 == player2):
        print("It's a tie!")

    elif(player1 == beats[player2]):
        print("Player 1 won!")

    elif(player2 == beats[player1]):
        print("Player 2 won!")

        play_game(player1, player2, beats)

main()
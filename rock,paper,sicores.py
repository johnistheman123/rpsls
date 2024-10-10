# project: test.py
#        author: Jonathan E Ouellette <jouellette2918061@woonsocketschools.com>
#  date written: 10/10/2024
#
#   description: rpsls

import random

print("""
=== RPS Duel === \n
    Challengers, step forward and prepare for an epic game!!!
""")

# === Get the names of our challengers
player1 = input("First Challenger, what is YOUR name? : ")
player2 = input("Second Challenger, state thy name or enter 'C' to practice against the computer: ")
weaponsFullName = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
computerPlayer = "Horatio the Chaotic Computer"
weapons = ["R", "P", "S", "L", "V"]
score1 = score2 = 0
wallet1 = wallet2 = 20

isPlaying = True

while isPlaying:
    # === Choose your move
    print("""
    On your table before you there are five choices :
        [R]ock : it's just a rock
        [P]aper: you can so many things with it
        [S]cissors: A weapon for cutting things
        [L]izard: A reptile from the jungle
        [V]Spock: A being of fiction
    """)
    bet1 = int(input(f"You have {wallet1} dollars in your wallet. How much do you want to bet? : "))
    wallet1 -= bet1
    weapon1 = input(f"{player1}, choose thy weapon! : ")
    if player2 == "C":  # Computer randomly chooses a weapon
        randomWeapon = random.randint(0, 4)
        weapon2 = weapons[randomWeapon]
        print(f"Horatio the Chaotic Computer chooses {weaponsFullName[randomWeapon]}")
        bet2 = 2
        print(f"Horatio the Chaotic Computer bets {bet2}! ")

    else:
        weapon2 = input(f"{player2}, choose thy weapon! : ")
        bet2 = int(input(f"You have {wallet2} dollars in your wallet. How much do you want to bet? : "))
        wallet2 -= bet2
    # === Resolve combat
    if weapon1 == "R":  # Player1 chooses Rock
        if weapon2 == "R":
            print("Thou hast ended in a Draw!")
        elif weapon2 == "P":
            print(f"Paper covers Rock! {player2} wins this round!")
            wallet2 += bet2*2
            score2 = score2 + 1
        elif weapon2 == "V":
            print(f"Spock vapourizes Rock with his phaser! {player2} wins this round!")
            score2 = score2 + 1
            wallet2 += bet2 * 2
        elif weapon2 == "L":
            print(f"Rock crushes Lizard! {player1} wins this round!")
            score1 = score1 + 1
            wallet1 += bet1 * 2
        else:  # weapon2 must be Scissors
            print(f"Rock crushes Scissors! {player1} wins this round!")
            score1 = score1 + 1
            wallet1 += bet1 * 2
    elif weapon1 == "P":  # Player1 chooses Paper
        if weapon2 == "P":
            print("Thou hast ended in a Draw!")
        elif weapon2 == "R":
            print(f"Paper covers Rock! {player1} wins this round!")
            score1 = score1 + 1
            wallet1 += bet1 * 2
        elif weapon2 == "V":
            print(f"Paper disprooves Spock! {player1} wins this round!")
            score1 = score1 + 1
            wallet1 += bet1 * 2
        elif weapon2 == "L":
            print(f"Lizard shreds Paper! {player2} wins this round!")
            score2 = score2 + 1
            wallet2 += bet2 * 2
        else:
            print(f"Scissors cut Paper! {player2} wins this round!")
            score2 = score2 + 1
            wallet2 += bet2 * 2

    elif weapon1 == "L":  # Player1 chooses Lizard
        if weapon2 == "L":
            print("Thou hast ended in a Draw!")
        elif weapon2 == "V":
            print(f"Lizard poisons Spock! {player1} wins this round!")
            score1 = score1 + 1
            wallet1 += bet1 * 2
        elif weapon2 == "P":
            print(f"Lizard eats Paper! {player1} wins this round!")
            score1 = score1 + 1
            wallet1 += bet1 * 2
        elif weapon2 == "R":
            print(f"Rock crushes Lizard! {player2} wins this round!")
            score2 = score2 + 1
            wallet2 += bet2 * 2
        else:
            print(f"Scissors decapitate Lizard! {player2} wins this round!")
            score2 = score2 + 1
            wallet2 += bet2 * 2
    elif weapon1 == "V":  # Player1 chooses Spock
        if weapon2 == "V":
            print("Thou hast ended in a Draw!")
        elif weapon2 == "S":
            print(f"Spock smashes Scissors! {player1} wins this round!")
            score1 = score1 + 1
            wallet1 += bet1 * 2
        elif weapon2 == "R":
            print(f"Spock vapourizes Rock with his phaser! {player1} wins this round!")
            score1 = score1 + 1
            wallet1 += bet1 * 2
        elif weapon2 == "L":
            print(f"Lizard poisons Spock! {player2} wins this round!")
            score2 = score2 + 1
            wallet2 += bet2 * 2
        else:
            print(f"Paper disproves Spock! {player2} wins this round!")
            score2 = score2 + 1
            wallet2 += bet2 * 2

    else:  # weapon1 must be Scissors
        if weapon2 == "S":
            print("Thou hast ended in a Draw!")
        elif weapon2 == "L":
            print(f"Scissors decapitate Lizard! {player1} wins this round!")
            score1 = score1 + 1
            wallet1 += bet1 * 2
        elif weapon2 == "P":
            print(f"Scissors cut Paper! {player1} wins this round!")
            score1 = score1 + 1
            wallet1 += bet1 * 2
        elif weapon2 == "V":
            print(f"Spock smashes Scissors! {player2} wins this round!")
            score2 = score2 + 1
            wallet2 += bet2 * 2
        else:
            print(f"Rock breaks Scissors! {player2} wins this round!")
            score2 = score2 + 1
            wallet2 += bet2 * 2
    print(f"{player1} hath scored {score1} points and {wallet1} dollars.")
    if player2 == "C":
        print(f"{computerPlayer} hath scored {score2} points and {wallet2} dollars.")
    else:
        print(f"{player2} hath scored {score2} points and {wallet2} dollars.")

    # == Play again?
    ask = input("Would you like another round? : ")
    if ask != "Y":
        isPlaying = False

if score1 > score2:
    print(f"{player1} win the duel with {score1} points!")
elif score2 > score1:
    if player2 == "C": player2 = computerPlayer
    print(f"{player2} win the GAME with {score2} points!")
else:
    print("The game end in a draw!")

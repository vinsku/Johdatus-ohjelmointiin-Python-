#onkotylsaa.py
#Answer Y or N:

def main():

    rivi = input("Bored? (y/n) ")

    answer = str(rivi)
    while answer not in ("Y","y","N","n"):
        print("Incorrect entry.")
        rivi = input("Please retry: ")
        answer = str(rivi)

    while answer in ("n","N"):
        rivi = input("Bored? (y/n) ")
        answer = str(rivi)

        while answer not in ("Y", "y", "N", "n"):
            print("Incorrect entry.")
            rivi = input("Please retry: ")
            answer = str(rivi)

    else:
        print("Well, let's stop this, then.")

main()
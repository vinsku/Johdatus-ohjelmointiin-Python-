def main():

    rivi = input("How do you feel? (1-10) ")
    fiilis = float(rivi)

    if fiilis > 7:
        rivi = str(":-)")
        print("A suitable smiley would be", str(rivi), )

    elif fiilis < 0:
        print("Bad input!")

    elif fiilis > 10:
        print("Bad input!")

    else:
        rivi = str(":-|")
        print("A suitable smiley would be", str(rivi), )

main()
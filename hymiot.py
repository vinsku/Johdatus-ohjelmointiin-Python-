def main():

    rivi = input("How do you feel? (1-10) ")
    fiilis = float(rivi)

    if fiilis == 10:
        rivi = str(":-D")
        print("A suitable smiley would be", str(rivi), )

    elif fiilis > 10:
        print("Bad input!")

    elif fiilis > 7:
        rivi = str(":-)")
        print("A suitable smiley would be", str(rivi), )

    elif fiilis == 1:
        rivi = str(":'(")
        print("A suitable smiley would be", str(rivi), )

    elif fiilis == 0:
        print("Bad input!")

    elif fiilis < 0:
        print("Bad input!")

    elif fiilis < 4:
        rivi = str(":-(")
        print("A suitable smiley would be", str(rivi), )

    elif fiilis > 10:
        print("Bad input!")

    else:
        rivi = str(":-|")
        print("A suitable smiley would be", str(rivi), )

main()
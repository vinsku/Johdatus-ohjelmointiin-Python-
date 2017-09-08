#vaihtorahalaskuri.py
#käytössä 1, 2, 5 ja 10 euron rahoja
#jos annetaan arvo 0 mitään ei tulosteta
#kokonaishinta aina tasaeuroja

def main():
    rahat = \
        [(10, "ten-euro notes"),
        (5, "five-euro notes"),
        (2, "two-euro coins"),
        (1, "one-euro coins")]

    hinta = int(input("Purchase price: "))
    maksettu = int(input("Paid amount of money: "))
    summa = maksettu - hinta

    if summa <= 0:
        print("No change")
    else:
        print("Offer change:")
        for raha in rahat:
            if summa >= raha[0]:
                print("{} {}".format(summa // raha[0], raha[1]))
                summa %= raha[0]


main()
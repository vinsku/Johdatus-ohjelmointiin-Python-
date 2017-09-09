def main():

    num = input("Anna numero:")

    while num <= 10:
        i = 1
        while i <= 100:
            product = num * i
            print(num, " * ", i, " = ", product, "\n")
            i = i + 1
        print("\n")
        num = num + 1
main()

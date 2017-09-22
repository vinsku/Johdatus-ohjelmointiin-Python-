def main():

    def laske_kulmat():

        kulmat = input("Anna kahden kulman arvot:")
        kulmat = kulmat.split(",")
        if len(kulmat) != 2:

            vastaus = 180 - int(kulmat[0])
            print(vastaus)
        else:

            kukkuu = 180 - int(kulmat[0]) - int(kulmat[1])
            print(kukkuu)


    laske_kulmat()
main()
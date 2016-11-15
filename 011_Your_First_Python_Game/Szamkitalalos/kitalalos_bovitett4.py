import random


def exit1():
    while True:
        new = input("Még egy játék? [\033[1mY/N\033[0m]:")
        if new == "Y" or new == "y":
           # exitVar = True
            break
        elif new == "N" or new == "n":
            print("\n\033[1mKilépés\033[0m")
            running = False
            exit()
        else:
            print("\n\033[1mÍrj Y vagy N karaktert!\033[0m \n")


def main():
    tippCounter = 1
    running = True

    while running:
        genRandNum = random.randrange(1, 101)
        print(
            "\n\033[1mGondoltam egy számra 1 és 100 között, 8 tipp-ből találd ki!\033[0m \n(X-re kilép!)\n")
        print(genRandNum)

        while tippCounter < 9:
            while True:
                userInput = input("{}. Tipp:".format(tippCounter))
                if userInput.isdigit():
                    userInput = int(userInput)
                    break
                elif userInput == "X" or userInput == "x":
                    print("\n\033[1mKilépés\033[0m")
                    exit()
                else:
                    print("\033[1mSzámot írj be!\033[0m")

            if userInput == genRandNum:
                print("\033[1mTalált :)\033[0m \n")
                exitVar = False
                tippCounter = 1
                genRandNum = random.randrange(1, 101)
                exit1()
                # if exitVar:
                #   break

            elif userInput < genRandNum:
                if (genRandNum - userInput) > 50:
                    print(
                        "\033[1mTe kis csintalan, jóval nagyobbra gondoltam!!!\033[0m")
                    tippCounter += 1
                else:
                    print("\033[1mNagyobbra gondoltam!\033[0m")
                    tippCounter += 1

            elif userInput > genRandNum:
                if (userInput - genRandNum) > 50:
                    print(
                        "\033[1mTe kis butuska, jóval kisebbre gondoltam!!!\033[0m")
                    tippCounter += 1
                else:
                    print("\033[1mKisebbre gondoltam!\033[0m")
                    tippCounter += 1

            if tippCounter == 9:
                print("\n\033[1mVesztettél :(\033[0m \n")
                #exitVar = False
                tippCounter = 1
                genRandNum = random.randrange(1, 101)
                exit1()
                # if exitVar:
                #   break

if __name__ == "__main__":
    main()

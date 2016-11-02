i = 1

while True:
    idea = input("What is your new idea: ")

    file = open("ideabank.txt", "w")

    file.write(idea)

    file.close()

    file = open("ideabank.txt", "r")

    print("{}. {}".format(i, file.read())

    i += i

# print("Your ideabank: \n", idea)


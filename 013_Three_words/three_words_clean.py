def checkio(string):
    words = string.split(" ")
    print(words)
    counter = 0

    for word in words:
        if word.isalpha() == True:
            counter +=1
        elif word.isalpha() == False:
            if counter >= 3:
                counter = 3
            elif counter < 3:
                counter = 0

    if counter >= 3:
        print("True") 
    elif counter < 3:
        print("False")

# Test:
checkio("Hello World hello hi 8 7 8")
checkio("Hello World hello") 
checkio("He is 123 man") 
checkio("1 2 3 4") 
checkio("bla bla bla bla")
checkio("Hi") 
checkio("1 2 3 4 klk lklk lklk") 
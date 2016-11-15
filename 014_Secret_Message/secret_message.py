def find_message(text):
    # text = input("Write the text for code it:")
    coded_text = ""
    for char in text:
        if char.isupper():
            coded_text += char
    print(coded_text)

    # Test:
find_message("How are you? Eh, ok. Low or Lower? Ohhh.")
find_message("hello world!")
find_message("hello Lisa, We GO!")

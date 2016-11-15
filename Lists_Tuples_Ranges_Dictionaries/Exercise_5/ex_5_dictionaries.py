telephone_book = {
"Jane Doe" : "+27 555 5367",
"John Smith" : "+27 555 6254",
"Bob Stone" : "+27 555 5689",
}

telephone_book["Jane Doe"] = "+27 555 1024"

telephone_book["Anna Cooper"] = "+27 555 3237"
# telephone_book.get("Anna Cooper", "+27 555 3237")

print(telephone_book["Bob Stone"])
#print("Bob Stone" in telephone_book)

print(telephone_book.get("Bob Stone", None))

print(telephone_book.keys())

print(telephone_book.values())
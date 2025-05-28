import inflect
p = inflect.engine()
for b in range(int(input("Enter a number: ")), -1, -1):  # or any number
    word = p.number_to_words(b).title()
    print(f"{word} green {p.plural('bottle', b)} sitting on the wall,")
    print(f"{word} green {p.plural('bottle', b)} sitting on the wall,")
    print("And if one green bottle should accidentally fall,")
    if b == 1:
        print("There’ll be no green bottles sitting on the wall")
    else:
        next_word = p.number_to_words(b - 1)
        print(f"There'll be {next_word} green {p.plural('bottle', b - 1)} sitting on the wall.")
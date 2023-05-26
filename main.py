PLACEHOLDER = "[name]"

with open("Input/Letters/starting_letter.txt") as data:
    first_line = data.read()
    with open("Input/Names/invited_names.txt") as names:
        for name in names:
            name = name.strip()
            with open(f"Output/ReadyToSend/Letter_to_{name}.txt", mode="w") as new_letter:
                individual_letter = first_line.replace(PLACEHOLDER, name)
                new_data = new_letter.write(individual_letter)


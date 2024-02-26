import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato = {row["letter"]: row["code"] for (idx, row) in data.iterrows()}

user_input = input("Enter a word: ").upper()
input_to_nato = [nato[letter] for letter in user_input]
print(input_to_nato)

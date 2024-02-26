
with open("./Input/Names/invited_names.txt", "r") as data:
    names = data.readlines()
with open("./Input/Letters/starting_letter.txt", mode="r") as invite_text:
    invitation = invite_text.read()

for name in names:
    new_name = name.split("\n")
    with open(f"./Output/readyToSend/letter_for_{new_name[0]}.txt", "w") as contacts:
        contacts.write(invitation.replace("[name]", new_name[0]))

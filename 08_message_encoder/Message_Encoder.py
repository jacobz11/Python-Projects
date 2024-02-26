alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(text, shift):
    encoded_word = ''
    for ltr in text:
        is_word_founded = False
        for ltr_idx in range(len(alphabet)):
            if alphabet[ltr_idx] == ltr:
                if ltr_idx + shift <= 25:
                    ltr_idx += shift
                else:
                    ltr_idx += shift - 26
                encoded_word += alphabet[ltr_idx]
                is_word_founded = True
            if is_word_founded:
                break
    print(f'The encoded text is: {encoded_word}')


def decode(text, shift):
    decoded_word = ''
    for ltr in text:
        is_word_founded = False
        for ltr_idx in range(len(alphabet)):
            if alphabet[ltr_idx] == ltr:
                ltr_idx -= shift
                decoded_word += alphabet[ltr_idx]
                is_word_founded = True
            if is_word_founded:
                break
    print(f'The encoded text is: {decoded_word}')


# if decision == 'encode':
#     encrypt(plain_text, shift_amount)
# elif decision == 'decode':
#     decode(plain_text, shift_amount)
# else:
#     print('Please check your inputs')


def caesar(text, shift, direction):
    caesar_word = ''
    for ltr in text:
        is_letter_founded = False
        if ltr not in alphabet:
            caesar_word += ltr
        for ltr_idx in range(len(alphabet)):
            if alphabet[ltr_idx] == ltr:
                if direction == 'encode':
                    if ltr_idx + shift <= 25:
                        ltr_idx += shift
                    else:
                        ltr_idx += shift - 26
                elif direction == 'decode':
                    ltr_idx -= shift
                caesar_word += alphabet[ltr_idx]
                is_letter_founded = True
            if is_letter_founded:
                break
    print(f'The {direction}d text is: {caesar_word}')


user_input = 'yes'
while user_input == 'yes':
    decision = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    plain_text = input("Type your message:\n").lower()
    shift_amount = int(input("Type the shift number:\n"))
    shift_amount %= 26
    caesar(plain_text, shift_amount, decision)
    user_input = input('Do you want to try again? Type yes if so\n')
    if user_input == 'no':
        print('Goodbye')
        break

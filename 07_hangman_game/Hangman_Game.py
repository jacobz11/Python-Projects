import random
import hangman_art
import word_list
chosen_word = random.choice(word_list.word_list)
display = []
print('Welcome to Hangman game! Have fun!')

for ltr in chosen_word:
    display.append('_')
print(display)

is_win = False
num_of_lives = 6
print(hangman_art.stages[num_of_lives])

while num_of_lives > 0:
    guess = input('Guess a letter: ').lower()
    for ltr_idx in range(len(chosen_word)):
        if guess == chosen_word[ltr_idx]:
            display[ltr_idx] = guess
    if guess not in display:
        num_of_lives -= 1
    print(display)
    print(hangman_art.stages[num_of_lives])
    if '_' not in display:
        is_win = True
        num_of_lives = -1
        print('You Won!')

if num_of_lives == 0:
    is_win = False
    print(f'You lost!\nThe word was: {chosen_word}!')

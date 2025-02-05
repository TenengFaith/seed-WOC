import random
word=["insta","reaction","market"]
chosen_word=random.choice(word)
guess=input("guess a letter...: ")
display=[]
for i in range(len(chosen_word)):
    display+='_'
print(display)
for position in range(len(chosen_word)):
    letter=chosen_word[position]
    if letter==guess:
        display[position]=guess
print(display)

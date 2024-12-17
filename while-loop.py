import random

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

number = random.randint(1,10)

isGuessRight = False

while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
        
#pseudocodificação
        
#Se o usuário não tiver adivinhado a resposta correta, entre no loop.

#Peça ao usuário um palpite.

#O palpite é o número correto?

#Se o palpite estiver correto, informe ao usuário que ele foi o palpite correto e saia do loop.

#Se o palpite estiver errado, diga ao usuário que foi o palpite errado e continue o loop.
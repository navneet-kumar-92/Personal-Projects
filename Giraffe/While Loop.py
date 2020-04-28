
i = 1
while i<10:
    print(i-1)
    i = i + 1
    i += 1

# Building a Guessing game

password = "girrafe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != password and not(out_of_guesses) :
    if guess_count < guess_limit:
        if guess_count >= 1:
            print("Sorry try again!")
        guess = input("Enter password: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Sorry you couldn't guess. Please contact admin!")
else:
    print("You guessed the password in " + str(guess_count) + " attempt(s)! Congrats :)")
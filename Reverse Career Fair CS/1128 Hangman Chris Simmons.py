#!/usr/bin/env python
import sys
alpha = ["a","b","c","d","e","f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]
while True:
    print "Enter your phrase.  "
    phrase = raw_input().upper()
    count = 0
    maximum = len(phrase)
    for letter in phrase:
        if letter in alpha:
            count += 1
        else:
            print "Letters please."
    if phrase == " " or phrase == "":
        print "You need characters that are not spaces."
    elif count == maximum:
        break
print "Let's play hangman!"
guesses = ''
guesslist = [" "]
guessesleft = 6
while guessesleft > 0:
    failed = 0             
    for char in phrase:      
        if char in guesses:
            sys.stdout.write(char)
        elif char == " ":
            sys.stdout.write(" ")
        else:
            sys.stdout.write("_")
            failed += 1    
    if failed == 0:
        print
        print "You win!"
        break
    print
    guess = raw_input("Guess: ").upper()
    if guess == " ":
        print "Nope."
    elif guess in guesslist:
        print "You've guessed that already!"
    elif len(guess) > 1 or len(guess) < 1 or guess.isdigit():
        print "Nope."
    elif guess not in phrase and guess.isalpha():  
        guessesleft -= 1        
        print "Nope."
        print "You have " + str(guessesleft) + ' guesses left.'
        guesslist.append(guess)
        if guessesleft == 0:
            print
            print "You lose!"
    elif not guess.isalpha():
        print "Guess a letter."
    if len(guess) == 1:
        if guess in phrase:
            guesslist.append(guess)
            guesses += guess
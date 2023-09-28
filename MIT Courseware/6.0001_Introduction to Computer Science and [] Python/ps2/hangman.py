# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    temp_guess = letters_guessed.copy() #converts the string into a list so I can manipulate it while checking the answer
    answer = ""
        
    #iterates through the length of both the guess and secret word, comparing each index to make sure all letters match regardless of order
    for x in range(len(secret_word)):
        
        for i in range(len(letters_guessed)):
            # print(i)
            
            if temp_guess[i] == secret_word[x]:
                answer += letters_guessed[i]
                temp_guess[i] == '!' #prevents repeating letters from ruining the final answer check
                
                #TESTER vvv
                # print("inside the answer check rn: "+answer)
    
    if (answer == secret_word):
        return True
    
    return False

#TEST SCRIPT
# secret = "cat"
# guess = ['a','p','l','p','e']
# # guess = ['a','p','l','b','e']
# guess = ['c','z','t', 'd', 'u']
# print(is_word_guessed(secret,guess))

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    printable_guessed_word = []
    
    temp_secret = list(secret_word)
    
    for z in range(len(secret_word)):
        printable_guessed_word.append("_ ") #sets up an empty list of underscores the same length as the secret word
        # print(printable_guessed_word) #For testing purposes
    
    for x in range(len(secret_word)):
        
        for i in range(len(letters_guessed)):
            if letters_guessed[i] == temp_secret[x]:
                printable_guessed_word[x] = letters_guessed[i]+" "
                # print(printable_guessed_word)
                break
    
    result = ''.join(printable_guessed_word)
    return result
                
# secret = "coochie"
# guess = ['c','c','h','c','d','e','i']
# print(get_guessed_word(secret,guess))


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    
    # print(string.ascii_lowercase)
    available_letters = list(string.ascii_lowercase) #gets all the lowercase letters in the alphabet and adds them to a list
    
    for i in range(len(available_letters)):
        for x in range(len(letters_guessed)):
            if letters_guessed[x] == available_letters[i]:
                available_letters[i] = ''
    result = ' '.join(available_letters)
    return result

# guess = ['z','b','c', 'e']
# print(get_available_letters(guess))       

def attempt_guess(character,secret_word):
    
    for i in range(len(secret_word)):
        if character == secret_word[i]:
            return True
        
    return False

#credit to chatGPT for this one! A handy method for checking if a character is a vowel
def is_vowel(character):
    vowels = "aeiou"
    return character in vowels #checks to see if the parameter exists within the vowels string

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    guesses = 6 #how many guesses the user starts with
    warnings = 4
    
    letters_guessed = []
    
    secret_word = choose_word(wordlist)
    
    #TESTERS VVVV
    # secret_word = "sensor"
    # print(secret_word)

    
    guessed_character = ''
    
    print("\n\nWelcome to hangman!")
    
    #TESTERS VVVV
    # teststring = 'T'
    # teststring2 = 't'
    # teststring3 = 4
    # print(str.isalpha(teststring))
    # print(str.isalpha(str(teststring3)))
    # print(str.lower(teststring))
    # print(str.isalpha(teststring2))
    
    
    while(guesses > 0):
        print("Available letters:\n"+get_available_letters(letters_guessed)+"\n")
        print(get_guessed_word(secret_word,letters_guessed)+"\n")
        
        inputting = True
        while inputting:
            #TOO HARSH! VVV The player doesnt lose when they run out of warnings. Instead, a guess is subtracted!
            # if (warnings <= 0):
            #     print("\nOkay, that's it! If you can't follow the rules, then you lose!")
            #     guesses = 0
            #     break
            
            guessed_character = str(input())
            guessed_character = str.lower(guessed_character)
            
            repeated = False
            for i in range(len(letters_guessed)):
                if guessed_character == letters_guessed[i]:
                    repeated = True
                    
            
            if not str.isalpha(guessed_character):
                warnings -= 1
                print("\nPlease enter a letter...  You have "+str(warnings)+" warnings left")
                if (warnings <= 0):
                    print("You lose a guess for that!")
                    guesses  -= 1
            elif (len(guessed_character) > 1):
                warnings -= 1
                print("\nPlease enter a single letter...  You have "+str(warnings)+" warnings left")
                if (warnings <= 0):
                    print("You lose a guess for that!")
                    guesses  -= 1
            elif(repeated):
                warnings -= 1
                print("\nPlease do not repeat letters...  You have "+str(warnings)+" warnings left")
                if (warnings <= 0):
                    print("You lose a guess for that!")
                    guesses  -= 1
            else:
                inputting = False
                
        
            
        
        failed_vowel = False
        if not attempt_guess(guessed_character,secret_word): #if the function returns false, the "not" allows me to do something!
            guesses -= 1
            if (is_vowel(guessed_character)):
                failed_vowel = True

            
        #if the user incorrectly guesses a vowel, another guess is lost!
        
        letters_guessed.append(guessed_character)
        
        #TESTER vvv
        # print(letters_guessed)
        
        score = 0
        
        if is_word_guessed(secret_word,letters_guessed):
            score =  guesses*len(secret_word)
            print("\nCONGRATULATIONS!\nThe hanged man lives today.")
            print(get_guessed_word(secret_word,letters_guessed))
            print("Your final score is: "+str(score))
            break
        
        # if (warnings <= 0):
        #      print("\n\nChances remaining: >:(")   
        # else:
        #     print("\n\nChances remaining: "+str(guesses))
        print("\n\n")
        if (failed_vowel):
            print("You lost two guesses for attempting an incorrect vowel!")
            guesses -= 1
        print("Chances remaining: "+str(guesses))

    
    if (guesses < 1):
        print("RIP... better luck next time!")
        print("(the word was "+secret_word+")")
        input()


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    
    spaceless_word = my_word.replace(" ","")
    #this would transform "p_ _ p" into "p__p"
    # TESTERS to make sure the word is converted properly
    # print(my_word)
    # print(spaceless_word)
    
    if (len(other_word) < len(spaceless_word)):
        return False
    
    repeat_letters = []
    #this creates a list (repeat_letters) that fills in "_" from my_word with the missing letter from other_word
    #example: the word "a_ple" is compared against "apple" to produce repeat_letters = "!p!!!"
    for i in range(len(spaceless_word)):
        if spaceless_word[i] != "_":
            repeat_letters.append("!")
        else:
            repeat_letters.append(other_word[i])

    #TESTER VVVV
    # print("repeated letters: "+str(repeat_letters))
    
    if len(spaceless_word) != len(other_word):
        return False
    
    matching = False
    
    for i in range(len(spaceless_word)):
        if spaceless_word[i] == "_":
            
            #checks the repeat_letters list at the same spot as "_" appears in the guessed word... 
            #if the letter that is supposed to fill the "_" appears elsewhere in the secret word, catches it!
            for x in range(len(other_word)):
                if repeat_letters[i] == other_word[x] and spaceless_word[x] != "_":
                    
                    #TESTER VVV
                    # print("repeat detected")
                    return False
            
        elif spaceless_word[i] == other_word[i]:
            matching = True
            
        else:
            return False

    return matching
                
#VARIOUS TESTERS VVV
# print(match_with_gaps("g_ d","god"))
# print(match_with_gaps("a_ ple","apple"))
# print (match_with_gaps("a_ e_ ","apes"))
# print (match_with_gaps("poo_ _ es ","poodles"))
# print (match_with_gaps("po_ _ _ es ","poodles"))
# print (match_with_gaps("te_ t","tact"))
# print (match_with_gaps("a_ _ le","banana"))
# print(match_with_gaps("a_ _ le","apple"))
# print(match_with_gaps("a_ ","a"))


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    possible_matches = []
    
    for i in range(len(wordlist)):
        if (match_with_gaps(my_word,wordlist[i])):
            possible_matches.append(wordlist[i])
            
    if len(possible_matches) <= 0:
        print("No matches found")
    else:
        print(str(possible_matches))
    
#TESTERS VVV 
# show_possible_matches("a_ _ le")  
# show_possible_matches("t_ _ t")  
# show_possible_matches("abbbb_ ")  
# show_possible_matches("a_ pl_ ")  

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    guesses = 6 #how many guesses the user starts with
    warnings = 4
    
    letters_guessed = []
    
    secret_word = choose_word(wordlist)
    
    #TESTERS VVVV
    # secret_word = "sensor"
    # print(secret_word)

    
    guessed_character = ''
    
    print("\n\nWelcome to hangman!")
    
    #TESTERS VVVV
    # teststring = 'T'
    # teststring2 = 't'
    # teststring3 = 4
    # print(str.isalpha(teststring))
    # print(str.isalpha(str(teststring3)))
    # print(str.lower(teststring))
    # print(str.isalpha(teststring2))
    
    
    while(guesses > 0):
        print("Available letters:\n"+get_available_letters(letters_guessed)+"\n")
        print(get_guessed_word(secret_word,letters_guessed)+"\n")
        
        inputting = True
        while inputting:
            #TOO HARSH! VVV The player doesnt lose when they run out of warnings. Instead, a guess is subtracted!
            # if (warnings <= 0):
            #     print("\nOkay, that's it! If you can't follow the rules, then you lose!")
            #     guesses = 0
            #     break
            
            guessed_character = str(input())
            guessed_character = str.lower(guessed_character)
            
            repeated = False
            for i in range(len(letters_guessed)):
                if guessed_character == letters_guessed[i]:
                    repeated = True
                    
            if guessed_character == '*':
                show_possible_matches(get_guessed_word(secret_word, letters_guessed))
                print("Your word is one of the words listed above. In light of this information, what will you guess next?")
            elif not str.isalpha(guessed_character):
                warnings -= 1
                print("\nPlease enter a letter...  You have "+str(warnings)+" warnings left")
                if (warnings <= 0):
                    print("You lose a guess for that!")
                    guesses  -= 1
            elif (len(guessed_character) > 1):
                warnings -= 1
                print("\nPlease enter a single letter...  You have "+str(warnings)+" warnings left")
                if (warnings <= 0):
                    print("You lose a guess for that!")
                    guesses  -= 1
            elif(repeated):
                warnings -= 1
                print("\nPlease do not repeat letters...  You have "+str(warnings)+" warnings left")
                if (warnings <= 0):
                    print("You lose a guess for that!")
                    guesses  -= 1
            else:
                inputting = False
                
        
            
        
        failed_vowel = False
        if not attempt_guess(guessed_character,secret_word): #if the function returns false, the "not" allows me to do something!
            guesses -= 1
            if (is_vowel(guessed_character)):
                failed_vowel = True

            
        #if the user incorrectly guesses a vowel, another guess is lost!
        
        letters_guessed.append(guessed_character)
        
        #TESTER vvv
        # print(letters_guessed)
        
        score = 0
        
        if is_word_guessed(secret_word,letters_guessed):
            score =  guesses*len(secret_word)
            print("\nCONGRATULATIONS!\nThe hanged man lives today.")
            print(get_guessed_word(secret_word,letters_guessed))
            print("Your final score is: "+str(score))
            break
        
        # if (warnings <= 0):
        #      print("\n\nChances remaining: >:(")   
        # else:
        #     print("\n\nChances remaining: "+str(guesses))
        print("\n\n")
        if (failed_vowel):
            print("You lost two guesses for attempting an incorrect vowel!")
            guesses -= 1
        print("Chances remaining: "+str(guesses))

    
    if (guesses < 1):
        print("RIP... better luck next time!")
        print("(the word was "+secret_word+")")
        input()




# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)

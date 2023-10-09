# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.
    
    word: string
    n: int >= 0
    n is the total number of letters in the hand when the word was entered (so, it includes the letters used in the current word)
    returns: int >= 0
    
    SCORE: 
    """
    
    score = 0
    
    word = word.lower() #converts the word to all lowercase
    word_length = len(word)
    
    sum_of_letters = 0
    
    for i in range (word_length):
        if (word[i] == '*'):
            sum_of_letters += 1
        else:
            sum_of_letters += SCRABBLE_LETTER_VALUES[word[i]]
        #TESTER VVV
        # print(sum_of_letters)
    
    second_component = 7*word_length-3*(n-word_length) #rewards the player for longer words and penalizes leftover letters in hand
    #TESTER VVV
    # print(str(sum_of_letters)+"+7*"+str(word_length)+"-3*("+str(n)+"-"+str(word_length)+")")
    if second_component < 1:
        second_component = 1
    
    score = sum_of_letters*second_component
    return score

#TESTER VVV
#Example: weed should be worth 176 with a hand size of 6
# print(get_word_score("weed",6))

# print(get_word_score("w*s",7))
# print(get_word_score("fork",4))
# print()
# print(get_word_score("honey",7))
# print(get_word_score("cows",6))
# print(get_word_score("wails",7))
# print()
# print(get_word_score("h*ney",7))
# print(get_word_score("c*ws",6))
# print(get_word_score("wa*ls",7))

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels):
        if (i == num_vowels - 1):
            x = '*'
        else:
            x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    #the parameters here mean i starts at num_vowels and ends at n, so basically consonants = difference between number of vowels and the total
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand

#TESTER VVVV
# display_hand(deal_hand(10))

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    new_hand = hand.copy()
    selected_key = 'a'
    
    word = word.lower()
    
    for i in range(len(word)):
        selected_key = word[i]
        
        #This checks to see if the specified key even exists in the dictionary before we run code on it (prevents keyError)
        if selected_key in new_hand:
             if new_hand[selected_key] > 1:
            
                 new_hand[selected_key] -= 1
            
             elif new_hand[selected_key] >= 0:
                del new_hand[selected_key]
                
        #Custom Aaron functionality that lets you automatically use up a * when you dont have enough vowels.. not in instructions!
        elif '*' in new_hand and word[i] in VOWELS:
            selected_key = '*'
            if selected_key in new_hand:
                 if new_hand[selected_key] > 1:
                
                     new_hand[selected_key] -= 1
                
                 elif new_hand[selected_key] >= 0:
                    del new_hand[selected_key]
            
    
    return new_hand

#TESTERS VVVV
# handOrig = {'a':1, 'n':1, 'l':2, 'm':1, 'u':1, 'd':1, '*':1}
# display_hand(handOrig)
# handNew = update_hand(handOrig,"almond")
# display_hand(handNew)

# handSpecial = {'b':1, 'q':1, 'l':2, 'i':1, 't':4, 'i':1}
# display_hand(handSpecial)
# handNuevo = update_hand(handSpecial,"liberal")
# display_hand(handNuevo)

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    #STEP 1: check if the selected word exists in the word list
    
    word = word.lower()
    wildcard_word = word
    
    gottem = False
    break_all_loops = False
    
    #this accounts for the wildcard (wildcard = *). It splices words from word_list with different vowels to see if the * placement is valid 
    for i in range(len(word)):
        if word[i] == '*':
            for x in range(len(VOWELS)):
                
                #The line below replaces the '*' with a vowel, and the for loop above tests every possible vowel in that index to create a valid word
                wildcard_word = word[:i] + VOWELS[x] + word[i+1:]
                
                for d in range(len(word_list)):
                    if word_list[d] == wildcard_word:
                        gottem = True
                        word = wildcard_word
                        break_all_loops = True
                        break
                    
                if break_all_loops:
                    break
                
        if break_all_loops:
            break
                        
    
    if not gottem:  
        for i in range(len(word_list)):
            if word_list[i] == word:
                gottem = True
                break
    
    #if gottem is False, the word does not exist in the word list
    if not gottem:
        print("\nThat word does not exist in the game's word bank.. sorry!\n")
        return False
    
    #STEP 2: check if the word can actually be composed out of the letters existing in the hand
    selected_key = 'a'
    
    checker_hand = hand.copy()
    
        # EXTRA CODE, may not use VVVV
        # or ('*' in checker_hand and word[i] in VOWELS):
        #      if selected_key in VOWELS and '*' in checker_hand:
        #          selected_key = '*'
    
    for i in range(len(word)):
        selected_key = word[i]
        
        if selected_key in checker_hand: 
             if checker_hand[selected_key] > 1:
            
                 checker_hand[selected_key] -= 1
            
             elif checker_hand[selected_key] >= 0:
                del checker_hand[selected_key]
              
        #Accounts for the wild card. If the selected index is a vowel and a * exists in the hand, subtract the * and keep going        
        elif '*' in checker_hand and word[i] in VOWELS:
            selected_key = '*'
            if checker_hand[selected_key] > 1:
            
                checker_hand[selected_key] -= 1
            
            elif checker_hand[selected_key] >= 0:
                del checker_hand[selected_key]
        
        else:
            print("\nYour hand doesn't even contain the letter "+selected_key+"!")
            return False
        
    return True

#TESTERS VVVV
# word_list = load_words()
# handOrig = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
# print(is_valid_word("quail", handOrig, word_list))

# handSpec = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
# print(is_valid_word("dog", handSpec, word_list))

# handSpec = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1, 'e':2}
# print(is_valid_word("lame", handSpec, word_list))

# handy = {'w':1, 'a':1, 'l':1, 'c':1, '*':1, 'x':1}
# handy = deal_hand(6)
#display_hand(handy)
# print(is_valid_word("c*w", handy, word_list))

# hand = {'n': 1, 'h': 1, '*': 1, 'y': 1, 'd':1, 'w':1, 'e': 2}
# word = "honey"
# print(is_valid_word(word, hand, word_list))

# hand = {'n': 1, 'h': 1, '*': 1, 'y': 1, 'd':1, 'w':1, 'e': 2}
# word = "h*ney"
# print(is_valid_word(word, hand, word_list))

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    length = 0
    
    # VOWELS
    # CONSONANT
    
    possible_keys = VOWELS+CONSONANTS+'*'
    # print(possible_keys)
    
    for i in range (len(possible_keys)):
        if possible_keys[i] in hand:
            
            length += hand[possible_keys[i]]
    
    return length

#TESTERS VVV
# hand = {'n': 3, 'h': 1, '*': 20, 'y': 1, 'd':1, 'w':1, 'e': 1}
# #length should be 8
# print(calculate_handlen(hand))

def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    
    # BEGIN PSEUDOCODE <-- Remove this comment when you implement this function
    # Keep track of the total score
    score = 0
    n = calculate_handlen(hand)
    # As long as there are still letters left in the hand:
    print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
    
    print("\nEnter a word created from the letters in your hand!\n(Type !! to end the game)\n")
    # Display the hand
    while n > 0:
        display_hand(hand)
        
        # Ask user for input
        print()
        inputting = True
        
        break_loop = False
        
        while (inputting):
            user_input = input()
        # If the input is two exclamation points:
            if (user_input == "!!"):
                break_loop = True
                break
            # End the game (break out of the loop)
            
        # Otherwise (the input is not two exclamation points):
            else:
            # If the word is valid:
                if (is_valid_word(user_input, hand, word_list)):
                    
                # Tell the user how many points the word earned,
                # and the updated total score
                    points = get_word_score(user_input, n)
                    score += points
                    print("\nGreat! The word "+user_input+" earned you "+str(points)+" points!\n(You now have "+str(score)+" points.)")
                    # update the user's hand by removing the letters of their inputted word
                    hand = update_hand(hand, user_input)
                    inputting = False
                    
            # Otherwise (the word is not valid):
                # Reject invalid word (print a message)
                else:
                    inputting = False
            
            n = calculate_handlen(hand)
            # if (n > 0):
            #     print()
            #     display_hand(hand)
           
    # Game is over (user entered '!!' or ran out of letters),
        if (break_loop or n <= 0):
            break
    # so tell user the total score
    print("\nYou earned a total of "+str(score)+" points!")
    # Return the total score as result of function
    return score


#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    new_hand = hand.copy()
    
    letter = letter.lower()
    
    all_letters = VOWELS+CONSONANTS
    
    new_letter = 'a'
    
    selecting = True
    
    if not letter in new_hand:
        return new_hand
    else:
        while (selecting):
            new_letter = random.choice(all_letters)
            # print(new_letter)
            if not new_letter in new_hand:
                selecting = False
        #VVV this pops out the old letter and replaces it with the new letter
        new_hand[new_letter] = new_hand.pop(letter)
        
    
    return new_hand

# hand = {'n': 3, 'h': 1, '*': 2, 'y': 1, 'd':1, 'w':1, 'e': 1}
# print(hand)
# print(substitute_hand(hand, 'y'))
    
   
    #accepts a string and then checks to see if the string says some type of yes! 
    #returns true or false
    
def check_affirmation(response):
    if (response == "OK" or response == "YES" or response == "Si" or response == "si" or response == "Yes" or response == "yes" or response == "Y" or response == "y" or response == "ay" or response == "Ok" or response == "OK" or response == "ok" or response == "k" or response == "K"):
        return True
    return False

#TESTERS VVV
# print(check_affirmation("no"))
# print(check_affirmation("y"))
# print(check_affirmation("YES"))
# print(check_affirmation(":P"))
    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    
    # print("play_game not implemented.") # TO DO... Remove this line when you implement this function
    
    print("\nHello, and welcome to Word Game!")
    print("\nUsing a hand of letters, construct words to earn points!\nLonger words are worth more points.")
    print("Letters are valued the same as Scrabble letters.")
    
    print("\nHow many hands will you play?\n")
    inputting = True
    hands = 0
    round = 0
    while (inputting):
        hands = input()
        if (hands.isdigit() and int(hands) == 1):
            print("\nOkay, you will play "+str(hands)+" round.")
            inputting = False
        elif (hands.isdigit() and int(hands) > 1):
            print("\nOkay, you will play "+str(hands)+" rounds.")
            inputting = False
            
        else:
            print("\nPlease take this seriously dude...\n")
    
    total_score = 0
    replay_available = True
    swap_available = True
    for i in range(int(hands)):

        round += 1
        print("\n\nROUND "+str(round)+"!")
        
        hand = deal_hand(HAND_SIZE)
        if (swap_available):
            print("\nYour hand:")
            display_hand(hand)
        
        if (swap_available):
            print("\nYou have a letter swap available...\nwould you like to swap a letter in your hand for a random new letter?\n")
            response = input()
            if  (check_affirmation(response)):
                print("\nWhich letter would you like to swap?\n")
                swap_available = False
                letter = input()
                hand = substitute_hand(hand, letter)
                # display_hand(hand)
            
        
        if (replay_available):
            #hard coded for only one replay. Could make all of this variable
            while (replay_available):
                round_score = 0
                # hand = deal_hand(HAND_SIZE)
                round_score += play_hand(hand,word_list)
                
                print("\nWould you like to replay that hand?")
                display_hand(hand)
                print("(You only get to do this once per session)\n")
                
                response = input()
                if  (check_affirmation(response)):
                    replay_available = False
                    round_score += play_hand(hand,word_list)
                else:
                    total_score += round_score
                    break
        else:
            # hand = deal_hand(HAND_SIZE)
            total_score += play_hand(hand,word_list)
    
    print("\nFinal score across "+str(hands)+" hands: "+str(total_score))
    print("Thank you for playing! :)")
        
    
#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    #AARON COMMENTED THIS OUT!!!!!!!!! Fix it man before submission
    word_list = load_words()
    play_game(word_list)

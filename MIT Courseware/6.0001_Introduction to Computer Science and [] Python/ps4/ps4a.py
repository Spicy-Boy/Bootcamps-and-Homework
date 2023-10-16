# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    
    permutations = []
    
    #base case
    if (len(sequence) == 1):
        permutations.append(sequence) #the single letter is added to the list.. see line 42 or so to see where this letter gets added
        return permutations
    
    #recursive case
    else:
        for i in range (len(sequence)):
            sequence_as_list = list(sequence)
            #below is how to swap items in a list
            sequence_as_list[0], sequence_as_list[i] = sequence_as_list[i], sequence_as_list[0]  #example: this for loop would create "abc bac cab" from abc
            
            new_sequence = ''.join(sequence_as_list[1:]) #appends the first letter of each iteration, so the loop for abc would create "abc"
            
            for i in get_permutations(new_sequence):
                permutations.append(sequence_as_list[0] + i)
                
        return permutations 
        #NOTE: This code has repeats in it......
    
        

#The ChatGPT proposed solution:
#NOTE: doesn't actually run for some reason
# def gpt_permutations(s):
#     # Base case: if the string has only one character, return it as a list
#     if len(s) == 1:
#         return [s]
#
#     # Recursive case: generate permutations for the rest of the string
#     permutations = []
#     for i in range(len(s)):
#         # Swap the current character with the first character
#         # and recursively generate permutations for the rest of the string
#         s_list = list(s)
#         s_list[0], s_list[i] = s_list[i], s_list[0]
#         new_string = ''.join(s_list[1:])
#         for i in get_permutations(new_string):
#             permutations.append(s_list[0] + i)
#
#     return permutations

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)
    
    example_one = "abc"
    example_two = "bust"
    example_three = "cat"
    
    print("~~~")
    print("Permutations for the word input \"abc\":")
    print("Expected: abc, acb, bac, bca, cab, cba\n")
    result = get_permutations(example_one)
    print("Result of method:\n"+str(result));
    print("~~~")
    
    
    print("~~~")
    print("Permutations for the word input \"bust\":")
    print("Expected: bust, buts, bsut, bstu, btus, btsu, ubst, ubts, usbt, ustb, utbs, utsb, sbut, sbtu, subt, sutb, stbu, stub, tbus, tbsu, tubs, tusb, tsbu, tsub\n")
    result = get_permutations(example_two)
    print("Result of method:\n"+str(result));
    print("~~~")
    
    print("~~~")
    print("Permutations for the word input \"cat\":")
    print("Expected: cat, cta, act, atc, tca, tac\n")
    result = get_permutations(example_three)
    print("Result of method:\n"+str(result));
    print("~~~")

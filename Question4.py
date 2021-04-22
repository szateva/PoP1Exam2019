""" Implement a function
longest_sequence(s)
which takes a non-empty string s containing smaller case letters only. Find the longest
sequence where the same letter occurs continuously in s. The function must return a
tuple (L,N) where L is the letter and N is the length of this longest sequence. If there
are several letters for which the longest continuous sequence has the same length, print
the required information for the smallest (alphabetically) letter. Do not import any
libraries.
Indicative test cases:
assert longest_sequence("dghhhmhmx") == ("h", 3)
assert longest_sequence("dhkkhhkkkt") == ("k", 3)
assert longest_sequence("abbbadddadd") == ("b", 3) """

def longest_sequence(s):
    length = 1
    max_length = length
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            letter = s[i]
            length +=1
            print("in if, checking letter: ", letter, "length: ", length)
            if length >= max_length:
                max_length = length
                max_letter = letter
                print("maximums are: ", max_letter, max_length)
        else:
            length = 1


    return (max_letter, max_length)
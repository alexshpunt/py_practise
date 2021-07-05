#Function which will return the cost of the mismatch characters 
#If they are identical the cost = 0
#If they are both vowels or consonants then the cost = 1
#Otherwise Cost = 3
def mismatch_cost(ch1, ch2):
    if ch1 == ch2: return 0 
    vowel = "aeiou"
    return 1.0 if (ch1 in vowel) == (ch2 in vowel) else 3.0

gapPenalty = 2.0 

tests = [
    ("mean", "name"),
    ("stop", "stop"),
    ("zaco", "azoc"),
    ("post", "stop"),
    ("stop", "tops"),
    ("ocurrance", "occurrence"),
    ("stop", "post"),
    ("ab", "abc"),
    ("abc", "ab"),
]
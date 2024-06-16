# your code goes here!

# pseudocode
# create a class called anagram
# have a word in put which will be in lower case
# create an object match that takes a list of words and have an emptyy list called matches list
# iterate over the words and convert them to lower case
class Anagram:
    def __init__(self, word):
        self.word = word.lower()
        self.sorted_word = ''.join(sorted(self.word))

    def match(self, words):
        matches = []
        for candidate in words:
            if ''.join(sorted(candidate.lower())) == self.sorted_word:
                matches.append(candidate)
        return matches



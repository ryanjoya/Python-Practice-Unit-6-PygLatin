pyg = 'ay'

original = raw_input('Enter a word:')
#User writes a word.

#Cleaned up if & print statements.

word = original.lower()
first = word[0]
new_word = word + first + pyg
#Concatenating variables.

new_word = new_word[1:len(new_word)]
print new_word
#User's word translated into PygLatin.

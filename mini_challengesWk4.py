# Oscar Leyva and Devin Branch


# String Methods Practice #1
#slieds 12 -16
# Print the following text in uppercase, using the specific string method:
# "Especially in electronic communications, writing in all caps is equivalent to yelling."
# sentence = "Especially in electronic communications, writing in all caps is equivalent to yelling."
sentence1 = "Especially in electronic communications, writing in all caps is equivalent to yelling."
print(sentence1.upper())

# String Methods Practice #2
# Join the following list into a string, separating each item with a space. Use the appropriate list/string method, and display the result.
# word_list = ["Simple","is","better","than","complex."]
word_list = ["Simple","is","better","than","complex."]
joined_sentence = " ".join(word_list)
print(joined_sentence)

# String Methods Practice #3
# Replace in the following sentence:
# "If the implementation is hard to explain, it might be a bad idea."
# the following pairs of words:
# "hard" --> "easy"
# "bad" --> "good"
# and display the sentence with both words modified.
new_sentence = "If the implementation is hard to explain, it might be a bad idea."
modified_sentence = new_sentence.replace("hard", "easy").replace("bad", "good")
print(modified_sentence)

# String Properties Practice #1
# Concatenate the text "Repetition" 15 times and display the result on the screen.
# Luckily, you know that strings are multipliable and you can do this activity in a simple and elegant way.

result = "Repetition " * 15
print(result)

# String Properties Practice #2
# Check if the word "beach" is not found in the following haiku. You should print the boolean.
# "Whitecaps on the bay:
# A broken signboard banging
# In the April wind."
# — Richard Wright, collected in Haiku: This Other World, 1998

beach = False
print(beach)


# String Properties Practice #3
# Check the Python Documentation to find the description of the len() function. Then, display on the screen the length (in number of characters) of the word electroencephalographist.
x = len("electroencephalographist")
print(x)
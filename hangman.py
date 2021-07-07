import random

##  find word bank from text file   ##
f = open("corpus.txt", "r")
initial_list = f.read().split()
nonWords = [",", ".", "-", "?", "!", ";", ":", "'", "(", ")", "[", "]", "{", "}",
            "=", "+", "/", "&", "$", "#", "@", "_", "<", ">", "%", "1", "2", "3",
            "4", "5", "6", "7", "8", "9", "0", '"']
wordList = []

for element in initial_list:
    if element not in nonWords:
        wordList.append(element)

word = wordList[random.randint(0, len(wordList))].lower()

def update(word, current, letter):
    #updates the current list and returns it
    temp = current.copy()
    if letter in word:
        for k in range(0, len(word)):
            if word[k] == letter:
                temp[k] = letter
        return temp
    return -1
def split(word):
    return [char for char in word]


#construct current list
current = []
for k in range(0, len(word)):
    current.append("_")


print(current)
count = 0
fail_list = []
while count < 6:
    letter = input("Enter letter:")
    while len(letter) != 1:
        letter = input("Please enter a single letter:")
    new = update(word, current, letter)
    if new == -1:
        fail_list.append(letter)
        print("Letters tried: " + str(fail_list))
        count += 1
    else:
        current = new
        print(current)
    if current == split(word):
        break

if current == split(word):
    print("Congrats! You got it!")
else:
    print("Sorry try again!")
    print("The word was: " + word)
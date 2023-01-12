import random
import string

n_words = 10

letters = string.ascii_lowercase
words = []
for i in range(0,n_words):
    words.append(''.join(random.choice(letters) for j in range(random.randint(3,10))))

print(Words)
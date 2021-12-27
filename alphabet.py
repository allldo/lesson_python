print('input')
word = input().lower()
alphabet = 'qwertyuiopasdfghjklzxcvbnm'
for i in alphabet:
    occurrences = word.count(i)
    if (occurrences !=0):
        print('letter', i, occurrences)
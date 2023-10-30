vowels=['a','e','i','o','u']
word=input("Enter a word:")
print("Vowels in given word are:")
for v in word:
    if v in vowels:
        print(v)
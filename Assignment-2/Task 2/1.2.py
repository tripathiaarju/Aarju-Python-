def longwords(wordlist, length):
    return (word for word in wordlist if len(word) >= length)

def main():
    words = input("Enter words, separated by spaces: ").split()
    length = int(input("Minimum length of words to keep: "))
    print("Words longer than {} are {}.".format(length,
          ', '.join(longwords(words, length))))
main()
'''OUTPUT
Enter words, separated by spaces: Aarju Tripathi is learning python
Minimum length of words to keep: 5
Words longer than 5 are Aarju, Tripathi, learning, python.
'''
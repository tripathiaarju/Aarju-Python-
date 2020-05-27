def vowel_check(char):
    if(char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U'):
        return True
    else:
        return False
char = input("Enter character: ");
if (char.isalpha() == False):
    exit();
if (vowel_check(char)):
    print(True);
else:
    print(False);

'''OUTPUT
Enter character: A
True
'''
t = str(input("Enter your text: "))

if t == t[::-1]:
    print("The word is palindrome")
else:
    print("The word is not palindrome")
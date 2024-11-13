def is_palindrome(word):
    if word == word[::-1]:
        print("Palindrome")
    else:
        print("Not palindrome")
  
        
word = str(input("Enter a word: "))
is_palindrome(word)

res = ""
word = "level"
def is_palindrome(i):
    if i == word:
        return

    is_palindrome(i-1)
    res += word[i]

print(is_palindrome(5))

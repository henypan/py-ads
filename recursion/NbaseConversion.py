__author__ = 'Henry Pan'


def toStr(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base, base) + convertString[n % base]


print toStr(256, 16)
print toStr(10, 2)
print toStr(103, 8)

### practise

def reverse(s):
    if len(s) <= 1:
        return s
    else:
        return s[-1] + reverse(s[:-1])

print reverse("Hello")
print reverse("Sugar")
print reverse("g")
print reverse("")


def is_palindrome(s):
    if s == reverse(s):
        return True
    else:
        return False

print is_palindrome("kayak")
print is_palindrome("aibohphobia")
print is_palindrome("clerk")
print is_palindrome("live not on evil")


def remove_punctuation(s):
    return ''.join(a for a in s if a.isalnum())

print is_palindrome(remove_punctuation("live not on evil"))



def reverse(text):
    return purge(text[::-1])


def purge(text):
    p_text = []
    text = list(text.lower())
    for i in (0, len(text) - 1):
        if (ord('a') <= ord(text[i]) <= ord('z')):
            p_text.append(text[i])
    return p_text


def is_palindrome(text):
    return purge(text) == reverse(text)


something = input("Enter text: ")

if is_palindrome(something):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")

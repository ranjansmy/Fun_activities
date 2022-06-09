message = "This is a meaningful sentence"
""" Method 1
translated = ''

i = len(message) - 1
while i >= 0:
    translated = translated + message[i]
    i = i -1 

print(translated)
"""
""" Method 2
def reverse(string):
    string = string[::-1]
    return string

print (reverse(message))

"""
# Method 3
def reverse(string):
    string = "".join(reversed(string))
    return string

print(reverse(message))

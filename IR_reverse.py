message = "This is a meaningful sentence"
"""
translated = ''

i = len(message) - 1
while i >= 0:
    translated = translated + message[i]
    i = i -1 

print(translated)
"""

def reverse(string):
    string = string[::-1]
    return string

print (reverse(message))

'''
Giraffe Language
every volews -> g
------------------
'''

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
        # if letter in "AEIOUaeiou"
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation.title()

print(translate(input("Enter the phrase to be translated: ")))
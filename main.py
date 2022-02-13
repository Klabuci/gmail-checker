import string


def symbol_checker(string,character):
    for i in range(len(character)):
        if character[i] in string and character[i] != '.' and character[i] != '-' and character[i] != '_':
            return True

special=string.punctuation


while True:
    contine = False
    gmail = input('Introdu adresa gmail: ')
    if gmail[-10::] == '@gmail.com':
        nume = gmail[:-10]
        contine = symbol_checker(nume , special)
        if contine == True:
            print('Adresa nu este valida pentru ca contine carctere speciale')
            continue
        else:
            print('adresa este valida')
            break
    else:
        print('Adresa este invalida')
        continue

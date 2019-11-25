

def run():
    word = str(input('Escribe una palabra: '))

    result = palindrome2(word)

    if result is True:
        print('La palabra "{}" Sí es un palíndromo.'.format(word))
    else:
        print('La palabra "{}" No es un palíndromo.'.format(word))


def palindrome2(word):
    # Notación slice() significa que inicia de atras hacia adelante
    reversed_word = word[::-1]

    if reversed_word == word:
        return True

    return False


def palindrome(word):
    reversed_letters = []

    for letter in word:
        reversed_letters.insert(0, letter)

    reversed_word = ''.join(reversed_letters)

    if reversed_word == word:
        return True

    return False


if __name__ == "__main__":
    run()

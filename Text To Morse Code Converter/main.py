
morse_dict = {'a': '·−', 'b': '−···', 'c': '−·−·', 'd': '−··', 'e': '·', 'f': '··−·', 'g': '−−·', 'h': '····',
              'i': '··', 'j': '·−−−', 'k': '−·−', 'l': '·−··', 'm': '−−', 'n': '−·', 'o': '−−−', 'p': '·−−·',
              'q': '−−·−', 'r': '·−·', 's': '···', 't': '−', 'u': '··−', 'v': '···−', 'w': '·−−', 'x': '−··−',
              'y': '−·−−', 'z': '−−··', '0': '−−−−−', '1': '·−−−−', '2': '··−−−', '3': '···−−', '4': '····−',
              '5': '·····', '6': '−····', '7': '−−···', '8': '−−−··', '9': '−−−−·', ' ': ' '}


print('Welcome to the Morse Code Text Converter!')
to_translate = input('Please type your message here (letters, numbers and spaces only): ').lower()

playing = True
while playing:
    translatable = False
    while not translatable:
        translatable = False
        for char in to_translate:
            if char not in morse_dict:
                translatable = False
            else:
                translatable = True

            if not translatable:
                to_translate = input(f"{char} is not a permitted character. "
                                     f"Please try again (letters, numbers and spaces only): ").lower()
                break

    translated = [morse_dict[char] for char in to_translate]
    morse_message = ""

    for char in translated:
        morse_message += char

    print(f"Your message in morse code is {morse_message}")
    answer = input("Would you like to encode another message? Y/N: ").upper()

    if answer == "N":
        playing = False
    elif answer == "Y":
        playing = True
    else:


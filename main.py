from morse_code import morse_code_dict, logo
from functions import cls, play_dit, play_dah, play_silent_dit

program_on = True

while program_on:
    print(logo)

    try:
        print(f'"{prompt}" in Morse Code:')
        print(output)
    except NameError:
        pass
    else:
        # play morse code translation (exclude if they are looking at Morse Code alphabet)
        if prompt != 'The Morse Code Library':
            for sound in output:
                if sound == '.':
                    play_dit()
                elif sound == '-':
                    play_dah()
                elif sound == ' ':
                    play_silent_dit()

    prompt = input('\nType something to convert to Morse Code: ')
    output = ''

    if prompt == 'help':
        option_prompt = input('\nType "quit" to exit the program and "code" to see the morse code table: ')
        if option_prompt == 'quit':
            print('Thanks for using my program! Goodbye.')
            program_on = False
        elif option_prompt == 'code':
            for key in morse_code_dict:
                prompt = 'The Morse Code Library'
                output += f'\n"{key}"  =  {morse_code_dict[key]}'
    else:
        for letter in prompt:
            if letter == ' ':
                # add two spaces for long pause between words
                output += '  '
            elif letter.title() in morse_code_dict:
                # convert to morse code and add to output string
                output += morse_code_dict[letter.title()]
                output += '   '
            else:
                print(f'{letter} is not a valid letter. Please include only letters, numbers, and basic punctuation.')
                output = ''
                break
    cls()

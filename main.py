from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ''
    if cipher_direction == 'decode':
        shift_amount *= -1
    for char in start_text:
        # Keep characters the same if they are not in alphabet
        if char not in alphabet:
            end_text += char
        else:
            # Using "% 26" will allow going past the index of 25
            end_text += alphabet[(alphabet.index(char) + shift_amount) % 26]
    print(f'{cipher_direction.capitalize()}d text: {end_text}')

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    # Continue program until user does not enter 'y' or 'yes'
    if input('Do you want to continue? ').lower() not in ['y', 'yes']:
        print('Goodbye')
        break

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(plaint_text, shift_amount, direction):
    endcode = ""
    if direction == 2:
        shift_amount *= -1
    
    for char in plaint_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            endcode += alphabet[new_position]
        else:
            endcode += char
    
    print(endcode)
    
should_continue = True

while should_continue:
    direction = int(input("Type 1 for Encrypt and 2 Decrypt: "))
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    shift %= 26
    caesar(text, shift, direction)
    
    result = input("Type 'yes' if you want to go again. Otherwise, type 'no'.")
    if result == "no":
        should_continue = False
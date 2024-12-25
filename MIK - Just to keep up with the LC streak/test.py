def caesar_cipher(s, k):
    k = k % 26 
    
    encrypted_str = ''

    for char in s:
        original_pos = ord(char) - ord('a')
        
        # Calculate the new position after the shift
        new_pos = (original_pos + k) % 26
        
        # Convert the new position back to a character
        new_char = chr(new_pos + ord('a'))
        
        # Add the new character to the result
        encrypted_str += new_char
        
    return encrypted_str

print(caesar_cipher('secret', 3))
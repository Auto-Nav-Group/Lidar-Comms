def convert_characters_to_decimal(characters):
    binary_combined = ""

    for char in characters:
        hex_value = hex(ord(char))[2:] 
        hex_subtracted = hex(int(hex_value, 16) - int('30', 16))[2:]
        binary = bin(int(hex_subtracted, 16))[2:].zfill(6)  
        binary_combined += binary

    decimal_equivalent = int(binary_combined, 2)

    return decimal_equivalent

characters = ['m', '2', '@', '0']
result = convert_characters_to_decimal(characters)
print(result)

def convert_decimal_to_character(decimal):
    binary = bin(decimal)[2:].zfill(24)  
    binary_segments = [binary[i:i+6] for i in range(0, len(binary), 6)]  
    hex_values = [hex(int(segment, 2))[2:] for segment in binary_segments]  
    hex_added = [hex(int(hex_value, 16) + int('30', 16))[2:] for hex_value in hex_values]  
    characters = [chr(int(hex_value, 16)) for hex_value in hex_added]  

    return ''.join(characters)  

decimal = 5432
result = convert_decimal_to_character(decimal)
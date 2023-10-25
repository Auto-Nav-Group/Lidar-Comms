"""Holds the conversions for Lidar communications (encoding and decoding)"""

def process_characters(char_list):
    """Process characters in the char_list and return the decimal value"""
    combined = []
    for char in char_list:
        print(char)
        hex_val = hex(ord(char))
        # hex_val = hex_val[2:]
        print(hex_val)
        # subtracted_hex = int(hex_val) - 30
        # print(subtracted_hex)
        # binary = bin(subtracted_hex)
        # binary = binary[2:]
        # print(binary)
        # decimal = int(binary, 2)
        # print(decimal)
        # combined.append(str(decimal))

    combined_string = "".join(combined)
    print(combined_string)


process_characters(['m', 'D'])
# TODO: fix the character thing not working with certains ones

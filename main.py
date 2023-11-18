import serial
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

def send_bytes_through_usb(string, port, baudrate):
    try:
        ser = serial.Serial(port, baudrate)
        
        bytes_to_send = string.encode()
        
        ser.write(bytes_to_send)
        
        ser.close()
        
        print("Bytes sent successfully!")
    except Exception as e:
        print("Error sending bytes:", str(e))

string_to_send = convert_characters_to_decimal(['m', '2', '@', '0'])
port_name = "COM1"  
baudrate = 9600 

send_bytes_through_usb(string_to_send, port_name, baudrate)

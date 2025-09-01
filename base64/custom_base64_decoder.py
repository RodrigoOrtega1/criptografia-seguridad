def custom_base64_decode(input_string):
    """ Decodifica una cadena codificada en base 64 como lo describe el siguiente articulo

    https://base64.guru/learn/base64-algorithm/decode

    Args:
        input_string (str): Una cadena codificada en base 64.

    Returns:
        str: La cadena decodificada.
    """
    base64_to_value = {
        "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7,
        "I": 8, "J": 9, "K": 10, "L": 11, "M": 12, "N": 13, "O": 14, "P": 15,
        "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20, "V": 21, "W": 22, "X": 23,
        "Y": 24, "Z": 25, "a": 26, "b": 27, "c": 28, "d": 29, "e": 30, "f": 31,
        "g": 32, "h": 33, "i": 34, "j": 35, "k": 36, "l": 37, "m": 38, "n": 39,
        "o": 40, "p": 41, "q": 42, "r": 43, "s": 44, "t": 45, "u": 46, "v": 47,
        "w": 48, "x": 49, "y": 50, "z": 51, "0": 52, "1": 53, "2": 54, "3": 55,
        "4": 56, "5": 57, "6": 58, "7": 59, "8": 60, "9": 61, "+": 62, "/": 63
    }

    indices = [base64_to_value[char] for char in input_string if char in base64_to_value]

    binary_values = [f"{index:06b}" for index in indices]

    concatenated_binary = "".join(binary_values)

    byte_groups = [concatenated_binary[i:i+8] for i in range(0, len(concatenated_binary), 8)]

    decoded_characters = [chr(int(byte, 2)) for byte in byte_groups if len(byte) == 8]

    decoded_string = "".join(decoded_characters)

    return decoded_string

def read_file_by_byte(filename):
    """ Lee un archivo por bytes

    Args:
        filename (str): El nombre del archivo
    """
    with open(filename, 'rb') as f:
        return f.read().decode('ascii')
    
def save_decoded_bytes(decoded_bytes, destination_filename):
    """ Guarda una cadena de bytes en un archivo

    Args:
        decoded_bytes (str): Cadena a guardar
        destination_filename(str): Nombre del archivo donde se guardara
    """
    with open(destination_filename, 'wb') as f:
        f.write(decoded_bytes.encode('latin1'))

def main():
    bytes = read_file_by_byte('file3.lol')
    decoded = custom_base64_decode(bytes)
    save_decoded_bytes(decoded, 'decoded_file3.mp4')

if __name__=="__main__":
    main()
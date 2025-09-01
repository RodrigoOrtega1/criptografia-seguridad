def custom_base64_encode(input_bytes):
    """
    Codifica una cadena codificada en base 64 como lo describe el siguiente articulo.

    https://base64.guru/learn/base64-algorithm/encode

    Args:
        input_string (str): La cadena a codificar.

    Returns:
        str: La cadena codificada en base 64.
    """
    value_to_base64 = (
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "abcdefghijklmnopqrstuvwxyz"
        "0123456789+/"
    )

    binary_string = ''.join(f"{byte:08b}" for byte in input_bytes)

    six_bit_groups = [binary_string[i:i+6] for i in range(0, len(binary_string), 6)]

    if len(six_bit_groups[-1]) < 6:
        six_bit_groups[-1] = six_bit_groups[-1].ljust(6, '0')

    eight_bit_groups = [f"00{group}" for group in six_bit_groups]

    indices = [int(bits, 2) for bits in eight_bit_groups]

    encoded_chars = [value_to_base64[index] for index in indices]

    padding = (4 - len(encoded_chars) % 4) % 4

    encoded_chars += ['='] * padding

    return ''.join(encoded_chars)

def main():
    with open('decoded_file3.mp4', 'rb') as f:
        file_bytes = f.read()
    encoded = custom_base64_encode(file_bytes)
    with open('custom_encoded_file.lol', 'w') as f:
        f.write(encoded)

if __name__=="__main__":
    main()
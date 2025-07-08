import argparse

def transform_byte(byte, key_bytes, decrypt=False):
    for key_byte in key_bytes:
        if 0x20 <= key_byte <= 0x50:
            delta = key_byte if decrypt else -key_byte
        elif 0x51 <= key_byte <= 0xFF:
            delta = -key_byte if decrypt else key_byte
        else:
            continue

        byte = (byte + delta) % 256
    return byte

def process_file(input_path, output_path, key, decrypt=False):
    key_bytes = bytearray(key.encode('latin1'))

    with open(input_path, 'rb') as f:
        data = bytearray(f.read())

    for i in range(len(data)):
        data[i] = transform_byte(data[i], key_bytes, decrypt)

    with open(output_path, 'wb') as f:
        f.write(data)

    print(f"{'Decryption' if decrypt else 'Encryption'} Completed: {output_path}")

if __name__ == "__main__":
    decryptList = ["decrypt", "d", "D", "Decrypt", "DECRYPT"]
    parser = argparse.ArgumentParser(description="\nEncrypt or Decrypt a File using Full-Key Transformation.")
    parser.add_argument("MODE", choices=["encrypt", "decrypt", "e", "d", "E", "D", "Decrypt", "Encrypt", "DECRYPT", "ENCRYPT"], help="Choose to Encrypt or Decrypt.")
    parser.add_argument("INPUT", help="Input file path")
    parser.add_argument("OUTPUT", help="Output file path")
    parser.add_argument("KEY", help="ASCII Key-String")

    args = parser.parse_args()

    process_file(args.INPUT, args.OUTPUT, args.KEY, decrypt=(args.MODE in decryptList))

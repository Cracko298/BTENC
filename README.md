# BTENC
- A custom encryption algorithm with variable key length support, that works differently from something like XOR Ciphers.

## Usage: 
```
py cli.py [MODE] [INPUT_FILE] [OUTPUT_FILE] [KEY]

    [MODE]        = Decrypt/Encrypt.
    [INPUT_FILE]  = Input File PATH.
    [OUTPUT_FILE] = Output File PATH.
    [KEY]         = Your Custom Key.

Example Usage (Encrypting):
    py cly.py encrypt ".\Examples\ExampleImage.jpg" ".\MyEncryptedImage.enc" "My 'Very-Cool' Key :3"

Example Usage (Decrypting):
    py cli.py decrypt ".\MyEncryptedImage.enc" ".\DecryptedExampleImage.jpg" "My 'Very-Cool' Key :3"
```

## Why?
- Haha- idek. I made my own [Video](https://github.com/Cracko298/LVideo) and [3D Model](https://github.com/Cracko298/Better-Binary-Model-Format) Format(s), so I decided a simple Encryption Cipher would be easy enough to make.

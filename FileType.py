#!/usr/bin/env python3
import sys

def read_file_header(path, header_length=8):
    with open(path, 'rb') as file:
        header = file.read(header_length)
    return header

def find_file_type(header):
    magic_numbers = {
        b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A': 'PNG',
        b'\xFF\xD8\xFF': 'JPEG',
    }

    for magic, file_type in magic_numbers.items():
        fdsf = str(header)
        magic = str(magic)
        if fdsf.startswith(magic):
            return file_type
    return f'Dateityp von {path} konnte nicht erkannt werden'

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <file_path>")
        sys.exit()

    file_path = sys.argv[1]
    header = read_file_header(file_path)
    result = find_file_type(header)
    f'Datei {file_path} ist vom Typ {result}'
    print(f'Datei {file_path} ist vom Typ {result}')



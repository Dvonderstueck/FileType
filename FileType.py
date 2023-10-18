#!/usr/bin/env python3
import sys
from typing import List

def read_file_header(path: str) -> bytes:
    with open(path, 'rb') as file:
        header = file.read()
    return header

def starts_with_binary(file_header: bytes, magic_file: bytes) -> bool:
    return file_header[:len(magic_file )] == magic_file 

def find_file_type(header: bytes) -> str:
    magic_numbers = {
        b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A': 'PNG',
        b'\xFF\xD8\xFF': 'JPEG',
    }

    for magic, file_type in magic_numbers.items():
        #if header.startswith(magic):
         if starts_with_binary(header, magic):
            return file_type
    raise ValueError("Unknown file type")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <file_path>")
        sys.exit()

    file_path = sys.argv[1]

    try:
        header = read_file_header(file_path)
        result = find_file_type(header)
        print(f'Datei {file_path} ist vom Typ {result}')
    except ValueError as e:
        print(f"Error: {e}")

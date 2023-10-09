def find_file_type(path):

    magic_numbers = {
        b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A': 'PNG',
        b'\xFF\xD8\xFF': 'JPEG',
    }

    with open(path, 'rb') as file:
        header = file.read(8)

        for magic, file_type in magic_numbers.items():
                if header.startswith(magic):
                    return f'Datei {path} ist vom Typ {file_type}'
        return f'Dateityp von {path} konnte nicht erkannt werden'
    

file_path = "/Users/dennis.vonderstueck/Downloads/fan-art-skull-kid-the-legend-of-zelda-majoras-mask-wallpaper-preview.jpg"
result = find_file_type(file_path)
print(result)


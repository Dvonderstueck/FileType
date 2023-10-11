import unittest
from FileType import find_file_type  

class TestFindFileType(unittest.TestCase):

    def test_png_magic_number(self):
        path = '/Users/dennis.vonderstueck/Downloads/image.png'
        result = find_file_type(path)
        expected_result = f'Datei {path} ist vom Typ PNG'
        self.assertEqual(result, expected_result)

    def test_jpeg_magic_number(self):
        path = '/Users/dennis.vonderstueck/Downloads/fan-art-skull-kid-the-legend-of-zelda-majoras-mask-wallpaper-preview.jpg'
        result = find_file_type(path)
        expected_result = f'Datei {path} ist vom Typ JPEG'
        self.assertEqual(result, expected_result)
    
    def test_unknown_file_type(self):
        path = '/Users/dennis.vonderstueck/Downloads/Dennis Macbook.docx'
        result = find_file_type(path)
        expected_result = f'Dateityp von {path} konnte nicht erkannt werden'
        self.assertEqual(result, expected_result)

class TestMagicNumber(unittest.TestCase):
    def test_jpeg_file(self):
        with open('test.jpg', 'wb') as file:
            file.write(b'\xFF\xD8\xFF')

        result = find_file_type('test.jpg')
        self.assertEqual(result, 'Datei test.jpg ist vom Typ JPEG')

    def test_png_file(self):
        with open('test.png', 'wb') as file:
            file.write(b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A')

        result = find_file_type('test.png')
        self.assertEqual(result, 'Datei test.png ist vom Typ PNG')

    def test_unknown_file(self):
        with open('test.unknown', 'wb') as file:
            file.write(b'\x00\x00\x00\x00\x00\x00\x00\x00')

        result = find_file_type('test.unknown')
        self.assertEqual(result, 'Dateityp von test.unknown konnte nicht erkannt werden')


if __name__ == '__main__':
    unittest.main()

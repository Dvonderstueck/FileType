import unittest
from FileType import find_file_type, read_file_header  

class TestFindFileType(unittest.TestCase):
    def test_png_magic_number(self):
        header = b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A'
        result = find_file_type(header)
        expected_result = 'PNG'
        self.assertEqual(result, expected_result)

    def test_jpeg_magic_number(self):
        header = b'\xFF\xD8\xFF'
        result = find_file_type(header)
        expected_result = 'JPEG'
        self.assertEqual(result, expected_result)

    def test_unknown_file_type(self):
        header = b'\x00\x00\x00\x00\x00\x00\x00\x00'  
        try:
            find_file_type(header)
        except ValueError as e:
            expected_result = 'Unknown file type'
            self.assertEqual(str(e), expected_result)


class TestMagicNumber(unittest.TestCase):
    def test_jpeg_file(self):
        header = b'\xFF\xD8\xFF'
        result = find_file_type(header)
        self.assertEqual(result, 'JPEG')

    def test_png_file(self):
        header = b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A'
        result = find_file_type(header)
        self.assertEqual(result, 'PNG')

    def test_unknown_file(self):
        header = b'\x00\x00\x00\x00\x00\x00\x00\x00'

        try:
            find_file_type(header)
        except ValueError as e:
            expected_result = 'Unknown file type'
            self.assertEqual(str(e), expected_result)

if __name__ == '__main__':
    unittest.main()

import unittest
from FileType import find_file_type, read_file_header, starts_with_binary  

class TestFindFileType(unittest.TestCase):
    def test_png_magic_number(self):
        header: bytes = b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A'
        result: str = find_file_type(header)
        expected_result: str = 'PNG'
        self.assertEqual(result, expected_result)

    def test_jpeg_magic_number(self):
        header: bytes = b'\xFF\xD8\xFF'
        result: str = find_file_type(header)
        expected_result: str = 'JPEG'
        self.assertEqual(result, expected_result)

    def test_unknown_file_type(self):
        header: bytes = b'\x00\x00\x00\x00\x00\x00\x00\x00'  
        try:
            find_file_type(header)
        except ValueError as e:
            expected_result: str = 'Unknown file type'
            self.assertEqual(str(e), expected_result)

class TestMagicNumber(unittest.TestCase):
    def test_jpeg_file(self):
        header: bytes = b'\xFF\xD8\xFF'
        result: str = find_file_type(header)
        self.assertEqual(result, 'JPEG')

    def test_png_file(self):
        header: bytes = b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A'
        result: str = find_file_type(header)
        self.assertEqual(result, 'PNG')

    def test_unknown_file(self):
        header: bytes = b'\x00\x00\x00\x00\x00\x00\x00\x00'

        try:
            find_file_type(header)
        except ValueError as e:
            expected_result: str = 'Unknown file type'
            self.assertEqual(str(e), expected_result)

class TestStartsWithBinary(unittest.TestCase):
    def test_starts_with_binary_true(self):
        file_header: bytes = b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A\xFF\xD8\xFF'
        magic_file: bytes = b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A'
        result: bool = starts_with_binary(file_header,  magic_file)
        self.assertTrue(result)

    def test_starts_with_binary_false(self):
        file_header: bytes = b'\xFF\xD8\xFF\x89\x50\x4E\x47\x0D\x0A\x1A\x0A'
        magic_file: bytes = b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A'
        result: bool = starts_with_binary(file_header, magic_file)
        self.assertFalse(result)

    def test_starts_with_binary_short(self):
        file_header: bytes = b'\x89\x50\x4E\x47\x0D'
        magic_file: bytes = b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A'
        result: bool = starts_with_binary(file_header, magic_file)
        self.assertFalse(result)

    def test_starts_with_binary_empty_string(self):
        file_header: bytes = b''
        magic_file: bytes = b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A'
        result: bool = starts_with_binary(file_header, magic_file)
        self.assertFalse(result)

    def test_starts_with_binary_both_empty_strings(self):
        file_header: bytes = b''
        magic_file: bytes = b''
        result: bool = starts_with_binary(file_header, magic_file)
        self.assertTrue(result)

    def test_starts_with_binary_long_slice(self):
        file_header: bytes = b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A'
        magic_file: bytes = b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A\xFF\xD8\xFF'
        result: bytes = file_header[:len(magic_file)] 
        self.assertEqual(result, file_header)




if __name__ == '__main__':
    unittest.main()

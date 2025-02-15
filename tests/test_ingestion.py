import unittest
from src.ingestion import file_ingestion

class TestFileIngestion(unittest.TestCase):
    def test_read_file_data(self):
        # Create a temporary file for testing
        with open('test_data.txt', 'w') as f:
            f.write("line1\nline2\n")
        # Update the configuration temporarily if needed
        data = file_ingestion.read_file_data()
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 2)

if __name__ == '__main__':
    unittest.main()

import unittest
from src.staging import data_validation

class TestDataValidation(unittest.TestCase):
    def test_validate_data(self):
        valid_record = {"id": "10", "value": "200.5"}
        invalid_record = {"id": "abc", "value": "xyz"}
        self.assertTrue(data_validation.validate_data(valid_record))
        self.assertFalse(data_validation.validate_data(invalid_record))

if __name__ == '__main__':
    unittest.main()

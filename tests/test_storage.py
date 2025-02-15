import unittest
import os
from src.storage import data_lake

class TestDataLakeStorage(unittest.TestCase):
    def test_upload_to_data_lake(self):
        # Since we don't want to actually upload during tests,
        # we could mock boto3 client. Here, we just check that the function runs.
        try:
            data_lake.upload_to_data_lake('data/staging/temp_data.json', 'test/temp_data.json')
            result = True
        except Exception as e:
            print(e)
            result = False
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()

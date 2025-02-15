import unittest
from src.processing import transformation, aggregation

class TestProcessing(unittest.TestCase):
    def test_transformation(self):
        record = {"id": 1, "value": 100}
        transformed = transformation.transform(record)
        self.assertEqual(transformed['value'], 100 * 1.5)  # Based on scale_factor

    def test_aggregation(self):
        records = [{"id": 1, "value": 100}, {"id": 2, "value": 200}]
        result = aggregation.aggregate(records)
        self.assertEqual(result['total_value'], 300)

if __name__ == '__main__':
    unittest.main()

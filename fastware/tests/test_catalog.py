import unittest
import json
import os
from fastware.catalog.apps import load_catalog # I'll implement this helper in a moment

class TestCatalog(unittest.TestCase):
    def test_catalog_loading(self):
        # This assumes apps.json exists and is valid JSON
        catalog_path = os.path.join(os.path.dirname(__file__), '..', 'catalog', 'apps.json')
        with open(catalog_path, 'r') as f:
            data = json.load(f)

        self.assertIsInstance(data, list)
        self.assertTrue(len(data) > 0)
        self.assertIn('name', data[0])
        self.assertIn('package_id', data[0])

if __name__ == '__main__':
    unittest.main()

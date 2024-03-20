import unittest
from unittest.mock import patch
from invent import update_inventory

class TestUpdateInventory(unittest.TestCase):
    @patch('invent.inventory', {"pommes": 30, "bananes": 15, "oranges": 10})
    def test_update_inventory_existing_item(self, mock_inventory):
        update_inventory("pommes", 5)
        # Assert the modified dictionary directly
        self.assertEqual(mock_inventory, {"pommes": 35, "bananes": 15, "oranges": 10})

if __name__ == '__main__':
    unittest.main()
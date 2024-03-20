import unittest
from unittest.mock import patch
from db_con import connect_to_db


class TestConnectToDB(unittest.TestCase):
    @patch("db_con.connect_to_db")
    def test_connect_to_db_successful(self, mock_connect_to_db):
        mock_connect_to_db.return_value = "Connection successful"
        result = connect_to_db("my_database")
        self.assertEqual(result, "Connection successful")

    @patch("db_con.connect_to_db")
    def test_connect_to_db_unsuccessful(self, mock_connect_to_db):
        mock_connect_to_db.side_effect = ConnectionError("Could not connect to the database")
        with self.assertRaises(ConnectionError):
            connect_to_db("other_database")


if __name__ == '__main__':
    unittest.main()

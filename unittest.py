import os
import unittest

class TestDemo(unittest.TestCase):
    def setUp(self):
        db_file_path = "./demo.db"
        if os.path.exists(db_file_path):
            os.remove(db_file_path)
        self.ctrl = Controller()
        print("Connect to a new database")

    def test_xx(self):
        pass

    def tearDown(self):
        self.ctrl.deinit()
        print("Disconnect from database")
        
if __name__ == '__main__':
    unittest.main()
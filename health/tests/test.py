import unittest
from src.app import check_health

class AppTests(unittest.TestCase):
    def test_app(self):
        """Simple health check"""
        env=['skill-edge','integration','staging','prod']
        skill=['skill-tv','skill-ecare']
        for i in env:
            for j in skill:
                self.assertEqual(check_health(i,j),200)
   
    def suite():
        _suite=unittest.TestSuite()
        _suite.addTest(AppTests('test_app'))
        return _suite
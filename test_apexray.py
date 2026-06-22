# test_apexray.py
"""
Tests for ApexRay module.
"""

import unittest
from apexray import ApexRay

class TestApexRay(unittest.TestCase):
    """Test cases for ApexRay class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ApexRay()
        self.assertIsInstance(instance, ApexRay)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ApexRay()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

# test_ratecache.py
"""
Tests for RateCache module.
"""

import unittest
from ratecache import RateCache

class TestRateCache(unittest.TestCase):
    """Test cases for RateCache class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = RateCache()
        self.assertIsInstance(instance, RateCache)
        
    def test_run_method(self):
        """Test the run method."""
        instance = RateCache()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

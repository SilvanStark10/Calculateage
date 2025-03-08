#!/usr/bin/env python3
"""
Test runner for Calculate Age application.
Discovers and runs all tests in the tests directory.
"""
import unittest
import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def run_tests():
    """Discover and run all tests in the tests directory."""
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover(start_dir='tests', pattern='test_*.py')
    
    test_runner = unittest.TextTestRunner(verbosity=2)
    result = test_runner.run(test_suite)
    
    # Return non-zero exit code if tests failed (for CI)
    return 0 if result.wasSuccessful() else 1

if __name__ == '__main__':
    sys.exit(run_tests()) 
import unittest

from organizingLargerPrograms.demo_reader.src import reader

class TestMultireader(unittest.TestCase):
    def test_initialization(self):
        reader.multireader.MultiReadeer('test_file.txt')
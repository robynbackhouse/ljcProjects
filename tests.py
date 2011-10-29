#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
# This test code was written jointly by myself and Jonathan Hartley (if I'm honest here, mainly by Jonathan..), who very kindly provided all the python expertise.
# His rather cool blog can be found here:  http://tartley.com/

from unittest import TestCase, main

from main import find_jack, has_pair, has_2pairs

class PokerTest(TestCase):

    def test_find_jack(self):
        self.assertEqual(find_jack('2h 5s 5c 9d Td Jc Ks'), 'Clubs')

    def test_has_pair(self):
        self.assertEqual(has_pair(''), False)
        self.assertEqual(has_pair('3d'), False)
        self.assertEqual(has_pair('3c 3d'), True)
        self.assertEqual(has_pair('3c 4d'), False)
        self.assertEqual(has_pair('2c 3c 4d'), False)
        self.assertEqual(has_pair('2c 2c 4d'), True)
        self.assertEqual(has_pair('2c 3c 3d'), True)
        self.assertEqual(has_pair('2c 4c 4d 5c'), True)

main()


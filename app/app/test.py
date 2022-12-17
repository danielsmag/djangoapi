from django.test import SimpleTestCase
from app import calc


class CalcTest(SimpleTestCase):
    """test the calc modul"""

    def test_add_numbers(self):
        res = calc.add(4, 5)
        self.assertEqual(res, 9)

    def test_sub_numbers(self):

        res = calc.subtract(10, 5)

        self.assertEqual(res, 5)

import unittest

from functionality.functionality import Nokia

class TestFunctionality(unittest.TestCase):

    def test_that_phonebook_starts_empty(self):
        nokia = Nokia("Fey", 0o7022334455)
        self.assertEqual(nokia.get_phonebook(), [])

    def test_that_you_can_add_a_number(self):
        nokia = Nokia("Fey", 0o7022334455)
        nokia.name = "Fey"
        nokia.number = 0o7022334455
        nokia.add_contact()

        self.assertEqual(nokia.phonebook[0]["Name"], "Fey")
        self.assertEqual(nokia.phonebook[0]["Number"], 0o7022334455)

    def test_that_you_can_add_multiple_numbers(self):
        nokia = Nokia("Fey", 0o7022334455)
        nokia.name = "Fey"
        nokia.number = 0o7022334455
        nokia.add_contact()
        nokia.name = "Tay"
        nokia.number = 0o7022334466
        nokia.add_contact()

        self.assertEqual(nokia.phonebook[0]["Name"], "Fey")
        self.assertEqual(nokia.phonebook[0]["Number"], 0o7022334455)
        self.assertEqual(nokia.phonebook[1]["Name"], "Tay")
        self.assertEqual(nokia.phonebook[1]["Number"], 0o7022334466)
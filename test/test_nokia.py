import unittest
from unittest.mock import patch
from functionality.functionality import Nokia


class TestPhonebookFunctionality(unittest.TestCase):

    def test_that_phonebook_starts_empty(self):
        nokia = Nokia()
        self.assertEqual(nokia.get_phonebook(), [])


    def test_that_you_can_add_a_number(self):
        nokia = Nokia()
        with patch("builtins.input", side_effect=["Fey", "07022334455"]):
            nokia.add_contact()

        self.assertEqual(nokia.phonebook[0]["Name"], "Fey")
        self.assertEqual(nokia.phonebook[0]["Number"], "07022334455")

    def test_that_you_can_add_multiple_numbers(self):
        nokia = Nokia()
        with patch("builtins.input", side_effect=["Fey", "07022334455","Tay", "07022334466"]):
            nokia.add_contact()
            nokia.add_contact()

        self.assertEqual(nokia.phonebook[0]["Name"], "Fey")
        self.assertEqual(nokia.phonebook[1]["Name"], "Tay")

    def test_that_you_can_delete_contact(self):
        nokia = Nokia()
        with patch("builtins.input", side_effect=["Anne", "07011223344"]):
            nokia.add_contact()
        with patch("builtins.input", side_effect=["number", "07011223344"]):
            result = nokia.delete_contact()

        self.assertEqual(result, "Contact deleted")

    def test_that_you_can_edit_contact(self):
        nokia = Nokia()
        with patch("builtins.input", side_effect=["anne", "07011223344"]):
            nokia.add_contact()
        with patch("builtins.input", side_effect=["07011223344", "Temi", "07011223322"]):
            nokia.edit_contact()

        self.assertEqual(nokia.phonebook[0]["Name"], "Temi")
        self.assertEqual(nokia.phonebook[0]["Number"], "07011223322")

    def test_that_you_cannot_edit_a_contact_that_doesnt_exist(self):
        nokia = Nokia()
        with patch("builtins.input", side_effect=["07011223344"]):
            nokia.add_contact()
        with self.assertRaises(Exception) as context:
            nokia.edit_contact()

        self.assertIn("Contact not found", str(context.exception))

class TestMessageFunctionality(unittest.TestCase):
    def test_that_messages_start_empty(self):
        nokia = Nokia()
        self.assertEqual(nokia.get_messages(), [])

    def test_that_you_can_send_messages_to_a_contact(self):
        nokia = Nokia()
        with patch("builtins.input", side_effect=["Feyi", "07011223344"]):
            nokia.add_contact()
        with patch("builtins.input", side_effect=["Feyi", "Hello Feyi, how are you doing?"]):
            result = nokia.send_messages()

        self.assertEqual(result, "Message sent successfully")

    def test_that_you_can_send_messages_to_a_contact_that_doesnt_exist_in_our_list(self):
        nokia = Nokia()
        with patch("builtins.input", side_effect=["07011223344", "Hello Beautiful"]):
            result = nokia.send_messages()

        self.assertEqual(result, "Message sent successfully")

    def test_that_you_can_delete_messages_with_name(self):
        nokia = Nokia()
        with patch("builtins.input", side_effect=["Anne", "07011223344"]):
            nokia.add_contact()
        with patch("builtins.input", side_effect=["name","Anne", "Hello Cutie"]):
            nokia.send_messages()
        with patch("builtins.input", side_effect=["Anne"]):
            result = nokia.delete_message()

        self.assertEqual(result, "Message deleted")

    def test_that_you_can_delete_messages_with_number(self):
        nokia = Nokia()
        with patch("builtins.input", side_effect=["Anne", "07011223344"]):
            nokia.add_contact()
        with patch("builtins.input", side_effect=["number","07011223344", "Hello Cutie"]):
            nokia.send_messages()
        with patch("builtins.input", side_effect=["07011223344"]):
            result = nokia.delete_message()

        self.assertEqual(result, "Message deleted")

    def test_that_you_can_delete_the_message_of_someone_not_on_your_contact_list(self):
        nokia = Nokia()
        with patch("builtins.input", side_effect=["number", "07011223344", "Hello Cutie"]):
            nokia.send_messages()
        with patch("builtins.input", side_effect=["07011223344"]):
            result = nokia.delete_message()

        self.assertEqual(result, "Message deleted")




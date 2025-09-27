from functionality.functionality import Nokia

nokia = Nokia("Fey", 0o7011223344)
menu = """


                            Menu


                             1 -> Phonebook
                             2 -> Messages
                             3 -> Chat
                             4 -> Call Register
                             5 -> Tones
                             6 -> Settings
                             7 -> Call Divert
                             8 -> Games
                             9 -> Calculator
                            10 -> Reminders
                            11 -> Clock
                            12 -> Profiles
                            13 -> SIM Services
"""

print(menu)
menu_page = int(input("Choose a menu option: "))

match menu_page:
    case 1:
        phonebook = """
            1 -> Search
            2 -> Add Contact
            3 -> Delete contact
            4 -> Edit contact
            0 -> Back to main menu
            """
        print(phonebook)
        phonebook_option = int(input("Select Phonebook Option: "))
        match phonebook_option:
            case 1 :
                nokia.get_phonebook()
            case 2 :
                nokia.add_contact()
            case 3:
                nokia.delete_contact()
            case 4:
                nokia.edit_contact()


from functionality import Nokia

nokia = Nokia()
while True:
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
                5 -> Show contacts
                0 -> Back to main menu
                """
            print(phonebook)
            phonebook_option = int(input("Select Phonebook Option: "))
            match phonebook_option:
                case 1 :
                    nokia.search_contacts()
                case 2 :
                    nokia.add_contact()
                    print("Contact Added Succeessfully")
                case 3:
                    nokia.delete_contact()
                    print("Contact Deleted Succeessfully")
                case 4:
                    nokia.edit_contact()
                    print("Contact Edited Succeessfully")
                case 5:
                    nokia.get_phonebook()
                case 0:
                    break
                case _:
                    print("Invalid option")
                    break
        case 2:
            messages = """
                        1 -> Check Messages
                        2 -> Send Message
                        3 -> Delete Message
                        0 -> Back to main menu
                        """
            print(messages)
            messages_option = int(input("Select Messages Option: "))
            match messages_option:
                case 1 :
                    nokia.check_messages()
                case 2:
                    nokia.send_messages()
                case 3:
                    nokia.delete_message()





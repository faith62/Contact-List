import pyperclip

class Contact:
    """
    Class that generates new instances of contacts.
    """

    contact_list = [] # Empty contact list all instances of the class. Here we create the contact_list variable that will be used to store our created contact objects .

    def __init__(self,first_name,last_name,number,email):

      # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = number
        self.email = email

    def save_contact(self): # save_contact method that is called on a contact object and appends it to our contact-list list.

      '''
      save_contact method saves contact objects into contact_list
      '''

      Contact.contact_list.append(self)

    def delete_contact(self):#create a delete_contact method that uses the remove() method to delete the contact object from the contact_list.

      '''
      delete_contact method deletes a saved contact from the contact_list
      '''

      Contact.contact_list.remove(self)

    @classmethod # Decorators allow you to make simple modifications to callable objects like functions, methods, or classes.nforms the python interpreter that this is a method that belongs to the entire class
    def find_by_number(cls,number): # cls referred to the entire class, and does not need to be passed in when we call the method.


        '''
        Method that takes in a number and returns a contact that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            Contact of person that matches the number.
        '''

        for contact in cls.contact_list:
            if contact.phone_number == number:
                return contact
    
    @classmethod
    def contact_exist(cls,number):
        '''
        Method that checks if a contact exists from the contact list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for contact in cls.contact_list:
            if contact.phone_number == number:
                    return True

        return False

    @classmethod
    def display_contacts(cls):
        '''
        method that returns the contact list
        '''
        return cls.contact_list
    
    @classmethod
    def copy_email(cls,number):
        contact_found = Contact.find_by_number(number)
        pyperclip.copy(contact_found.email)

      
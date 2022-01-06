class Parent:
    def __init__(self, protected_variable, private_variable):
        self._protected = protected_variable
        self.__private = private_variable

    def get_protected(self):
        print("The Protected variable is ", self._protected)

    def get_private(self):
        print("The Private variable is ", self.__private)

    def set_protected(self, new_protected):
        self._protected = new_protected
        print("The value of the Protected variable was changed to ", self._protected)

    def set_private(self, new_private):
        self.__private = new_private
        print("The value of the Private variable was changed to ", self.__private)


# class Child:

if __name__ == '__main__':
    class1 = Parent(25, 57)
    class1.get_private()
    class1.get_protected()
    class1.set_private(44)
    class1.set_protected(77)

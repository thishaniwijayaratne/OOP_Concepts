class Parent:
    def __init__(self, protected_variable, private_variable):
        print("Parent class constructor function___________________________________________________________")
        self._protected = protected_variable
        self.__private = private_variable

    def get_protected(self):
        print("The Protected variable in ", type(self).__name__, " is ", self._protected)

    def get_private(self):
        print("The Private variable in ", type(self).__name__, " is ", self.__private)

    def set_protected(self, new_protected):
        self._protected = new_protected
        print("The value of the Protected variable was changed to ", self._protected, "by Parent.")

    def set_private(self, new_private):
        self.__private = new_private
        print("The value of the Private variable was changed to ", self.__private, "by Parent.")


class Child(Parent):
    def __init__(self, protected_variable, private_variable):
        print("Child class constructor function___________________________________________________________")
        self._protected = protected_variable
        self.__private = private_variable

    def get_protected(self):
        print("The Protected variable in", type(self).__name__, " is ", self._protected)

    def set_protected(self, new_protected):
        self._protected = new_protected
        print("The value of the Protected variable was changed to ", self._protected, "by child.")


if __name__ == '__main__':
    Parent_class = Parent(11, 22)
    Child_class = Child(33, 44)

    Child_class.get_protected()
    Parent_class.get_private()
    Parent_class.get_protected()

    Child_class.set_protected(55)
    Parent_class.set_private(66)
    Parent_class.set_protected(77)

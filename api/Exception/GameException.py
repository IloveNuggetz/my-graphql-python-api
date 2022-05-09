
class GameException(Exception):
    variable_class = 3

    def __init__(self, code, message):
        super().__init__(message)
        self.code = code

    def get_class_variable(self):
        global variable_class
        print(self.variable_class)
        return variable_class


obj = GameException(253, "messaage")
print(obj.__dict__)
print(vars(obj))

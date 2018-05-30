
print("file_a.py is getting executed")

# Note this gets set when the file is loaded
global_A = 'global_A (in file_a)'

class A(object):

    def __init__(self, attr, gb):

        print "instantiating an A object"

        # This attr is passed to the constructor
        self.attr = attr

        # These don't exist locally, so better exist in the global namespace
        self.myglobal_A = global_A
        self.myglobal_B = gb

    def __str__(self):
        """A pretty printer"""
        return "A(attr={}, global_A={}, global_B={})".format(
                self.attr, 
                self.myglobal_A,
                self.myglobal_B)

    def say_something(self):
        print "Hi! I'm {}".format(self)


class B(object):

    def __init__(self, attr, gb):

        print "instantiating a B object"

        # This attr is passed to the constructor
        self.attr = attr

        # These don't exist locally, so better exist in the global namespace
        self.myglobal_A = global_A
        self.myglobal_B = gb

    def __str__(self):
        """A pretty printer"""
        return "B(attr={}, global_A={}, global_B={})".format(
                self.attr, 
                self.myglobal_A,
                self.myglobal_B)

    def say_something(self):
        print "Hi! I'm {}".format(self)


if __name__ == '__main__':

    print "entering the __main__ block (file_a)"

    # Note this gets set when the __main__ block runs
    global_B = 'global_B'

    a = A('123 from file_a main', global_B)
    b = B('xzy from file_a main', global_B)

    a.say_something()
    b.say_something()

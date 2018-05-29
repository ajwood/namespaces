print("file_b.py is getting executed")

from file_a import A
from file_a import B

# Note this gets set when the file is loaded
global_A = 'global_A (in file_b)'

class C(object):
    
    def __init__(self, attr):

        print "instantiating a C object"

        # This attr is passed to the constructor
        self.attr = attr

        # These don't exist locally, so better exist in the global namespace
        self.myglobal_A = global_A
        self.myglobal_B = global_B


if __name__ == '__main__':

    print "entering the __main__ block (file_b)"

    # Note this gets set when the __main__ block runs
    global_B = 'global_B (in file_b)'

    a = A('123 from file_a main')
    b = B('xzy from file_a main')

    a.say_something()
    b.say_something()

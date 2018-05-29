# namespaces

$ python file_a.py
file_a.py is getting executed                # the file gets loaded
entering the __main__ block (file_a)         # at the bottom, we enter the main block
instantiating an A object                    # instantiate a couple objects
instantiating a B object                     # ...
Hi! I'm A(attr=123 from  file_a main, global_A=global_A (in file_a), global_B=global_B)   # call some methods
Hi! I'm B(attr=xzy from file_a main, global_A=global_A (in file_a), global_B=global_B)    # ...


$ python file_b.py
file_b.py is getting executed               # the file is getting loaded
file_a.py is getting executed               # we reached an import in file_b (loading A)
entering the __main__ block (file_b)        # note that file_a was only loaded once (and its main never ran)
instantiating an A object                   # instantiate an object
Traceback (most recent call last):          # since file_a.py's main never ran, it doesn't have a global_B
  File "file_b.py", line 36, in <module>
    a = A('123 from file_a main')
  File "/home/andrew/Programming/scratch/python/namespaces/file_a.py", line 18, in __init__
    self.myglobal_B = global_B
NameError: global name 'global_B' is not defined

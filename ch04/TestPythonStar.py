__author__ = 'jack'

#*args, **kwargs as the parameter, convert input to tuple/dict
def test_var_args(farg, *args):
    print "formal arg:", farg
    for arg in args:
        print "another arg: ", arg

def test_var_kwargs(farg, **kwargs):
    print "formal arg:", farg
    for key in kwargs:
        print "another keyword arg: %s: %s" %(key, kwargs[key])

test_var_args(1, "two", 3)
test_var_kwargs(1, arg2="two", arg3=3)

# *args, **kwargs as the real parameter(input), will explode the tuple/dict to elements
def test_var_args_call(arg1, arg2, arg3):
    print "arg1:", arg1
    print "arg2:", arg2
    print "arg3:", arg3

args = [2, 3]
test_var_args_call(1, *args) # test_var_args_call(1, 2, 3)

kwargs = {'arg3': 3, 'arg2' : 2}
test_var_args_call(1, **kwargs)  #test_var_args_call(1, arg2=2, arg3=3)

# together

def foo(bar=2, baz=5):
    print bar, baz

def proxy(x, *args, **kwargs):
    print x
    foo(*args, **kwargs)

proxy(6)   # just normal argument
proxy(7, 5) # normal + tuple + dict(empty)
proxy(8, bar='asdas') #normal + tuple(empty) + dict
proxy(9, baz='asdas') #normal + tuple(empty) + dict
proxy(23, 5, baz='foo') #normal + tuple + dict

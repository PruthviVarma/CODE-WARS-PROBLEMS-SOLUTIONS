def hello(name=""):
    if(name==""):
        return "Hello, World!"
    else:
        return 'Hello, ' + name.capitalize() + '!'
        
#test.assert_equals(hello(), "Hello, World!") to resolve this error when no 
#argument is passed try the def hello(name="")

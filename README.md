# python-tail - Unix tail follow implementation in Python #

## Installation ##

python setup.py install

## Basic Usage ##
    import tail
    
    # Create a tail instance
    t = tail.Tail('file-to-be-followed')

    # Register a callback function to be called when a new line is found in the followed file. 
    # If no callback function is registerd, new lines would be printed to standard out.
    t.register_callback(callback_function)

    # Follow the file with 5 seconds as sleep time between iterations. 
    # If sleep time is not provided 1 second is used as the default time.
    t.follow(s=5)
     

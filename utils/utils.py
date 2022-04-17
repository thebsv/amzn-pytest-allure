import inspect

#CONSTANTS

URL = "https://amazon.com/"

#FUNCTIONS

#function to get the name of current function being used
def whoami():
    return inspect.stack()[1][3]
import inspect

#CONSTANTS

URL = "https://amazon.com/"
USERNAME = "bhargav.srinivasan93@gmail.com"
PASSWORD = "Bhar00912**"

#FUNCTIONS

#function to get the name of current function being used
def whoami():
    return inspect.stack()[1][3]

import inspect

#CONSTANTS

URL = "https://amazon.com/"
USERNAME = "python.sriracha@gmail.com"
PASSWORD = "Van!!ock450,."

#FUNCTIONS

#function to get the name of current function being used
def whoami():
    return inspect.stack()[1][3]
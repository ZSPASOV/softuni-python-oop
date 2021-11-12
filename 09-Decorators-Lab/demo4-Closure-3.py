# Python allows a nested function to access the outer scope of the enclosing function
# This is called closure and is a critical concept in decorators

# v1
def print_message(message):
    def message_sender():
        "Nested Function"
        print(message)
    message_sender()

print_message("Some random message") # Some random message


# v2
def print_message(message):
    def message_sender():
        "Nested Function"
        print(message)
    return message_sender()

print_message("Some random message") # Some random message

# v3
def print_message(message):
    def message_sender():
        "Nested Function"
        print(message)
    return message_sender

print_message("Some random message")() # Some random message






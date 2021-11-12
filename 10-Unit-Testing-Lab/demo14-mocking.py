# In simple English, Mocking is make a replica or imitation of something
# In programming an object that you want to test may have dependencies on other complex objects
# Used to:
#     simulate the behavior of the real objects
#     isolate the behavior of an object
# Based on the 'action -> assertion' pattern
# Designed for use with unittest

# In unit testing we want to test methods of one class in isolation, but classes are not isolated
# They are using services and methods from other classes
# We mock the services and methods from other classes and simulate the real behavior

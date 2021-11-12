# A region in a program where a namespace is directly accessible
# In most of the cases there are at least three nested scopes:
# The innermost which is searched first
# The scopes of any enclosing functions
# The next-to-last scope (module's global names)
# The outermost (built-in names)

def scopes():
    def local_scope():
        text = "local text"  # local scope

    def nonlocal_scope():
        nonlocal text
        text = "nonlocal text"  # nonlocal scope

    def global_scope():
        global text
        text = "global text"  # global scope

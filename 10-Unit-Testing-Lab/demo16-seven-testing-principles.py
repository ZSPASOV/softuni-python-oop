# 1 Testing is context dependent
    # Testing is done differently in different contexts
# Example:
    # Safety-critical software is tested differently from an e-commerce site

# 2 Exhaustive testing is impossible
    # All combinations of inputs and preconditions are usually almost infinite number
    # Testing everything is not feasible
        # Except for trivial cases
    # Risk analysis and priorities should be used to focus testing efforts

# 3 Early testing is always preferred
    # Testing activities shall be started as early as possible
        # And shall be focused on defined objectives
    # The later a bug is found – the more it costs!


# 4 Defect clustering
    # Testing effort shall be focused proportionally
        # To the expected and later observed defect density of modules
# A small number of modules usually contains most of the defects discovered
    # Responsible for most of the operational failures


# 5 Pesticide paradox
    # Same tests repeated over and over again tend to lose their effectiveness
    # Previously undetected defects remain undiscovered
    # New and modified test cases should be developed

# 6 Testing shows presence of defects
    # Testing can show that defects are present
    # Cannot prove that there are no defects
    # Appropriate testing reduces the probability for defects

# 7 Absence-of-errors fallacy
    # Finding and fixing defects itself does not help in these cases:
    # The system built is unusable
    # Does not fulfill the user needs and expectations
#

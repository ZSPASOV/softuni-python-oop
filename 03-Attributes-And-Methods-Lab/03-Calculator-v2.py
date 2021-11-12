class Calculator:

    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        result = 1
        for n in args:
            result *= n
        return result

    @staticmethod
    def divide(*args):
        result = 1
        for n in args:
            if result > 1:
                result /= n
            else:
                result = n
        return result

    @staticmethod
    def subtract(*args):
        result = 0
        i = 0
        for n in args:
            if i == 0:
                result = n
            else:
                result -= n

            i += 1
        return result

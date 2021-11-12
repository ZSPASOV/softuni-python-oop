class Student:
    def __init__(self, name, id):
        self.id = id
        self.name = name

    def get_name(self):
        return self.name


# CRUD operations - create, read, update, delete
class StudentDAO: #DAO - data abstraction object
    def create(self, student):
        # Store student in the database
        pass

    def read(self, id):
        # get record by ID
        pass

    def update(self, id, updated_student):
        pass


class StudentMySQLDAO(StudentDAO):
    pass


class StudentMongoDBDAO(StudentDAO):
    pass

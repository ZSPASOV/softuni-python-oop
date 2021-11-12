from abc import ABC, abstractmethod


class DataSource(ABC):
    @abstractmethod
    def writeData(self, data):
        pass

    @abstractmethod
    def readData(self) -> str:
        pass



class FileDataSource(DataSource):
    def __init__ (self, filename):
        self._file = filename

    def writeData(self, data):
        # write data to file.
        pass

    def readData(self) -> str:
        # read data from file.
        pass


class EncryptionDecorator(DataSource):
    def writeData(self, data):
        # encrypt the data
        # pass encrypted data to wrapper
        pass

    def readData(self) -> str:
        # get encrypted data
        # decrypt it
        # return it
        pass

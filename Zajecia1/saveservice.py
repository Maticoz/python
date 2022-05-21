
from serialization import Serialization


class SaveService:
    @staticmethod
    def save(filename, data):
        if(type(data) is str):
            file=open(filename, "w")
            file.write(data)
            file.close()
        else:
            Serialization.write(filename, data)
        print("Data saved")

    @staticmethod
    def load(filename):
        data    =   Serialization.load(filename)
        return data

import pickle


class Serialization:
    @staticmethod
    def write(filename, data):
        file = open(filename, "wb")
        pickle.dump(data, file)
        file.close()

    @staticmethod
    def load(filename):
        return pickle.load(open(filename, "rb"))

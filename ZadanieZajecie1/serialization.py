import pickle


class Serialization:
    def write(filename, data):
        file = open(filename, "wb")
        pickle.dump(data, file)
        file.close()

    def load(filename):
        return pickle.load(open(filename, "rb"))

class Memory:
    def __init__(self):
        self.logs = []

    def store(self, item):
        self.logs.append(item)

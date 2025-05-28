class ListManager:
    def __init__(self):
        self.data = []

    def add_item(self, item):
        self.data.append(item)

    def remove_item(self, item):
        if item in self.data:
            self.data.remove(item)

    def calculate_average(self):
        if len(self.data) == 0:
            return 0
        total = sum(self.data)
        return total / len(self.data)

    def display_data(self):
        for item in self.data:
            print(item)

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for item in self.data:
                file.write(str(item) + '\n')

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                self.data.append(float(line.strip()))

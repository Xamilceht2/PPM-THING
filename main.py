class PPMimage:
    def make_list(self, file):
        temp = []
        row = int(self.dimensions.split()[1])
        for val in range(row):
            for pixel in range(3):
                temp.append(file(val))
        print(temp)
    def __init__(self, input, output):
        self.values = []
        self.magic_num = ''
        self.dimensions = ''

        with open(input) as file:
            self.magic_num = file.readline()
            self.dimensions = file.readline()
            self.make_list(file)
    def print(self):
        print(self.magic_num, self.dimensions)
test = PPMimage("squares.ppm", "out.ppm")

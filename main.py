class PPMimage:
    def make_list(self, file:str):
        counter = -1
        temp = file.split()
        row = int(self.dimensions.split()[1])
        for val in range(row):
            pass
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

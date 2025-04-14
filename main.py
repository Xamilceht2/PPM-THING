import math
class PPMimage:

    def row_from_list(self, row):
        counter = 0
        new_row = []
        pixel = []
        for value in row:
            counter += 1
            pixel.append(value)
            if counter >= 3:
                new_row.append(pixel)
                counter = 0
                pixel = []
        return new_row
    
    def make_list(self, file:str):
        row = []
        width = int(self.dimensions.split()[0])
        colors = []

        for line in file:
            line_list = line.strip().split()
            colors += line_list
        while len(colors) > 0:
            row = colors[:width*3]
            colors = colors[width*3:]
            pixel_row = self.row_from_list(row)
            self.values.append(pixel_row)
                
    def __init__(self, input, output):
        self.values = []
        self.magic_num = ''
        self.dimensions = ''
        self.maxval = ''
        self.output = output

        with open(input, 'r') as file:
            self.magic_num = file.readline()
            self.dimensions = file.readline()
            self.maxval = file.readline()
            self.make_list(file)

    def negate_red(self):
        for row in self.values:
            for pixel in row:
                red = int(pixel[0])
                red = (red - int(self.maxval)) * (-1)
                pixel[0] = str(red)

    def flip_hori(self):
        for row in self.values:
            row.reverse()
    
    def grey_scale(self):
        grey = 0
        for row in self.values:
            for pixel in row:
                for color in pixel:
                    grey += int(color)
                grey = math.floor(grey/3)
                pixel[0] = str(grey)
                pixel[1] = str(grey)
                pixel[2] = str(grey)
        
    def flatten_red(self):
        red = '0'
        for row in self.values:
            for pixel in row:
                pixel[0] = red

    def write_outfile(self):
        with open(self.output, 'w') as outfile:
            outfile.write(self.magic_num)
            outfile.write(self.dimensions)
            outfile.write(self.maxval)
            for row in self.values:
                for pixel in row:
                    for color in pixel:
                        outfile.write(color + ' ')
                outfile.write('\n')

    def print(self):
        print(self.magic_num, self.dimensions)
        for row in self.values:
            print(row)
test = PPMimage("cake.ppm", "out.ppm")
#test.negate_red()
#test.flip_hori()
#test.grey_scale()
#test.flatten_red()
test.write_outfile()
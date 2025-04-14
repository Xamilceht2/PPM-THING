class PPMimage:
    def make_list(self, file:str):
        pcounter = 0
        pixel = []
        row = []
        rcounter = 0
        row_val = int(self.dimensions.split()[1]) * 3
        carry = []
        for line in file:
            temp = carry
            carry = []
            temp += line.split()
            rcounter += len(temp)
            #print(temp, rcounter)
            if rcounter > row_val:
                remaining = rcounter - row_val
                for excess in range(remaining):
                    carry.append(temp[-excess])
                del temp[-remaining:]
            
            for color in temp:
                pcounter += 1
                pixel.append(color)
                if pcounter == 3:
                    row.append(pixel)
                    pcounter = 0
                    pixel = []
            self.values.append(row)
            #print(row)
            row = []     
            rcounter = 0
            
            
        
                
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
test = PPMimage("test.ppm", "out9.ppm")
#test.flip_hori()
test.write_outfile()
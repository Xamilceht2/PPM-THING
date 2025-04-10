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
            if rcounter >= row_val:
                if rcounter > row_val:
                    remaining = rcounter - row_val
                    for excess in range(remaining):
                        carry.append(temp[-excess])
                    del temp[-remaining:]
                self.values.append(row)
                row = []
                
                rcounter = 0
            for color in temp:
                pcounter += 1
                pixel.append(color)
                if pcounter == 3:
                    #print(pixel)
                    row.append(pixel)
                    pcounter = 0
                    pixel = []
            
            
        
                
    def __init__(self, input, output):
        self.values = []
        self.magic_num = ''
        self.dimensions = ''
        self.maxval = ''

        with open(input) as file:
            self.magic_num = file.readline()
            self.dimensions = file.readline()
            self.maxval = file.readline()
            self.make_list(file)
            self.values.pop(0)
        with open(output) as outfile:
            pass
    def print(self):
        print(self.magic_num, self.dimensions, self.values)
test = PPMimage("test.ppm", "out.ppm")
test.print()
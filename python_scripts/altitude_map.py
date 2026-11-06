from random import randint, uniform

class Terrain(object):

    def __init__(self, size:int, roughness:float):
        self.matrix = []
        self.roughness = roughness
        self.N = 2 ** size + 1
        for _ in range(self.N):
            row = []
            for k in range(self.N):
                row.append(None)
            self.matrix.append(row)
        self.assigned_matrix = True

    def diamond_square(self, amplitude) :

        self.matrix[0][0] = randint(0, 50)
        self.matrix[0][self.N-1] = randint(0, 50)
        self.matrix[self.N-1][0] = randint(0, 50)
        self.matrix[self.N-1][self.N-1] = randint(0, 50)

        step = self.N - 1
        while step > 1:
            # Diamond step
            for y in range(0, self.N - step, step):
                for x in range(0, self.N - step, step):
                    mid_point_value = (self.matrix[y][x] + 
                                    self.matrix[y][x+step] + 
                                    self.matrix[y+step][x] + 
                                    self.matrix[y+step][x+step])/4

                    self.matrix[y+step//2][x+step//2] = mid_point_value + uniform(-amplitude, amplitude)

            # Square step
            for cy in range(step//2, self.N, step):
                for cx in range(step//2, self.N, step):
                    for point in [(step//2 ,0), (-step//2,0), (0, step//2), (0,-step//2)]:
                        px = cx + point[0]
                        py = cy + point[1]

                        if px >= 0 and px < self.N and py >= 0 and py < self.N and self.matrix[py][px] == None:
                            count = 0 
                            summing = 0

                            for side_point in [(step//2 ,0), (-step//2,0), (0, step//2), (0,-step//2)]:
                                nx = px + side_point[0]
                                ny = py + side_point[1]
                                if nx >= 0 and nx < self.N and ny >= 0 and ny < self.N and self.matrix[ny][nx] != None:
                                    summing += self.matrix[ny][nx]
                                    count += 1
                            if count > 0:
                                self.matrix[py][px] = summing/count + uniform(-amplitude, amplitude)


            amplitude *= self.roughness
            step //= 2


    def check_altitude(self, row, col):
        return self.matrix[row][col]

    def check_amount_of_rows(self):
        return len(self.matrix)

    def check_amount_of_columns(self):
        return len(self.matrix[0])

    def save_altitude_map(self, path):

        with open(path, 'w') as map_file:

            map_file.write(f'{self.check_amount_of_columns()} {self.check_amount_of_rows()}\n')
            for row in self.matrix:
                for col in row:
                    map_file.write(f'{col:.0f} ')
                map_file.write('\n')

    def load_altitude_map(self, path):
        
        with open(path, 'r') as txt_file:

            content = txt_file.read()
            tolken = content.split()

            r = int(tolken[0])
            c = int(tolken[1])
            new_matrix = tolken[2:]

        i = 0

        # Unnalocating matrix if it's assigned.

        if self.assigned_matrix:
            self.matrix = []
            for _ in range(r):
                row = []
                for k in range(c):
                    row.append(new_matrix[i])
                    i += 1
                self.matrix.append(row)


        else:
            for row in len(self.matrix):
                for col in len(row):
                    self.matrix[row][col] = new_matrix[i]
                    i += 1




        


                


                            

    




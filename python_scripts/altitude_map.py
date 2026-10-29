from random import randint, uniform

class Terrain(object):

    def __init__(self, size:int, roughness:float):
        self.matrix = []
        self.roughness = roughness
        self.N = 2 ** size + 1
        for _ in range(N):
            row = []
            for k in range(N):
                row.append(None)
            self.matrix.append(row)

    def diamond_square(self, amplitude) :

        self.matrix[0][0] = randint(0, 30)
        self.matrix[0][self.N-1] = randint(0, 30)
        self.matrix[self.N-1][0] = randint(0, 30)
        self.matrix[self.N-1][self.N-1] = randint(0, 30)

        step = self.N - 1
        # Diamond step
        while step > 1:
            for y in range(0, self.N, step):
                for x in range(0, self.N, step):
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
                    

    




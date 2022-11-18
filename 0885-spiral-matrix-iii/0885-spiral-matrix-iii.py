class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        coordinates = [ [rStart, cStart] ]
        total_cells = (rows * cols) - 1
        
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        step_amount = 1
        
        cur_i = rStart
        cur_j = cStart
        
        cur_dir_index = 0
        
        while total_cells > 0:
            for _ in range(step_amount):
                cur_i += directions[cur_dir_index][0]
                cur_j += directions[cur_dir_index][1]
                if cur_i >= 0 and cur_i < rows and cur_j >= 0 and cur_j < cols:
                    coordinates.append([cur_i, cur_j])
                    total_cells -= 1
            
            if cur_dir_index % 2 == 1:
                step_amount += 1
                
            cur_dir_index = (cur_dir_index + 1) % 4
        
        return coordinates
def optimal(matrix, target):
    '''first, take row wise cumulative sum'''

    ROWS = len(matrix)
    COLS = len(matrix[0])

    for row in range(ROWS):
        for col in range(1, COLS): #kyunke pehle col ka same sum hi hoga uska cumsum
            matrix[row][col] += matrix[row][col - 1]

    #Now,you need to find number of subarrays that equal sum == target, leetcode 560 - downwards direction

    result = 0

    for startCol in range(COLS):

        for j in range(startCol, COLS):

            hash = {0 : 1} #aik dafa zero to dekha hi hai
            cumSum = 0
            for row in range(ROWS):
                cumSum += matrix[row][j] - (matrix[row][startCol - 1] if startCol > 0 else 0)
                if cumSum - target in hash:
                    result += hash[cumSum - target]
                if cumSum in hash:
                    hash[cumSum] += 1
                else:
                    hash[cumSum] = 1
    return result
def optimal(matrix):
    '''Go from left to right, top to bottom
    right to left, bottom to top'''
    n = len(matrix)
    m = len(matrix[0])

    left = top = 0
    right = m - 1
    down = n - 1
    ans = []

    id = 0
    '''    //id
        //0   -> left  to right
        //1   -> top   to down
        //2   -> right to left
        //3   -> down  to top '''
    
    while left <= right and top <= down:
        #left to right
        if id == 0:
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            top += 1

        # top to bottom
        if id == 1:  
            for i in range(top, down + 1):
                ans.append(matrix[i][right])

            right -= 1
        if id == 2:
            for i in range(right, left - 1, -1):
                ans.append(matrix[down][i])
            down -= 1
        if id == 3:
            for i in range(down, top - 1, -1):
                ans.append(matrix[i][left])
            left += 1
        id = (id+1) % 4

    print(ans)

optimal([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

'''1 2 3 4
   5 6 7 8
 9 10 11 12'''
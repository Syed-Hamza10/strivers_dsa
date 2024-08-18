def brute(arr1, arr2): #TC O(n1 x n2) SC (n2)
    '''arr1 me iteration kre ge or arr2 ke against aik visited array bana le ge
    agar arr2 ka pehla index interesection me include hogya to use 1 krde ge and now that can't be considered
    as next potential element'''

    visited = [0] * len(arr2)
    intersection = []

    for i in range(len(arr1)):

        for j in range(len(arr2)):

            if arr1[i] == arr2[j] and visited[j] == 0:
                intersection.append(arr1[i])
                visited[j] = 1
                break

            if arr2[j] > arr1[i]: 
                break

    return intersection

print(brute([1,2,3,4,5,6],[3,4,4,5,6]))


def optimal(arr1, arr2):

    i = 0
    j = 0
    interesection = [ ]

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1

        elif arr2[j] < arr1[i]:
            j += 1

        else: # mean both of them are equal so put anyone you want
            interesection.append(arr1[i])
            i += 1
            j += 1 

    return interesection   

print(optimal([1,2,3,4,5,6],[3,4,4,5,6]))
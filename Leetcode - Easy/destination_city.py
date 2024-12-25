def approach1(paths):

    hash = {}
    n = len(paths)
    for ele in paths:
        if ele[0] not in hash:
            hash[ele[0]] = 1
    for ele in paths:
        if ele[1] not in hash:
            return ele[1]
        
    return

print(approach1([["A","Z"]]))
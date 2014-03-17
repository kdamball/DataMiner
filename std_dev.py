def manhattan(vector1, vector2): 
    """Computes the Manhattan distance.""" 
    distance = 0 
    total = 0 
    n = len(vector1) 
    for i in range(n): 
        distance += abs(vector1[i] - vector2[i]) 
    return distance 
    
def get_median(arr):
    arr.sort()
    
    if len(arr)%2 == 1:
        return arr[(len(arr)-1)/2]
    else:
        return (arr[len(arr)/2]+arr[(len(arr)-1)/2])/2.0


def computeNearestNeighbor(itemName, itemVector, items): 
     """creates a sorted list of items based on their distance to item""" 
     distances = [] 
     for otherItem in items: 
        if otherItem != itemName: 
            distance = manhattan(itemVector, items[otherItem]) 
            distances.append((distance, otherItem)) 
     # sort based on distance -- closest first 
     distances.sort() 
     return distances
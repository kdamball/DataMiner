from math import sqrt

users = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
         "Bill":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
         "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
         "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
         "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
         "Jordyn":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
         "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
         "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}
        }

def manhattan(user1, user2):
    distance = 0
    for key in user1:
        if key in user2:
            distance += abs(user1[key] - user2[key])
    return distance
    
def minkowski(ratings1, ratings2, r):
    distance = 0
    commonRatings = False
    for key in ratings1:
        if key in ratings2:
            distance += pow(abs(ratings1[key] - ratings2[key]), r)
            commonRatings = True
    if commonRatings:
        return pow(distance, 1/r)
    else:
        return 0 #no ratings in common
    
def getNearestNeighbour(user, others):
    distances = []
    for each in others:
        if user != others[each]:
            distance = minkowski(others[each], user, 2)
            distances.append((distance, each))
    distances.sort()
    return distances

def recommend(user,others):
    bestMatch = getNearestNeighbour(user, others)[0][1]
    bandsToRecommend = []
    for band in others[bestMatch]:
        if not band in user:
            bandsToRecommend.append(band)
    return bandsToRecommend
            
def pearson(user1, user2):
    xySum, xSum, ySum, x2Sum, y2Sum, n = 0,0,0,0,0,0
    for key in user1:
        if key in user2:
            n += 1
            xSum += user1[key]
            ySum += user2[key]
            xySum += user1[key]*user2[key]
            x2Sum += user1[key]**2
            y2Sum += user2[key]**2
            denominator = sqrt(x2Sum - ((xSum**2)/n)) * sqrt(y2Sum - ((ySum**2)/n))
    if n == 0 or denominator == 0:
        return 0
    else:
        return (xySum - ((xSum*ySum)/n)) / denominator
            
    



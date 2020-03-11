import math

def Euclidean(x, y):
    return math.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)


def GreatCircle(x, y):
    R = 6371
    phi1 = math.radians(x[0])
    phi2 = math.radians(y[0])
    phi = math.radians(y[0] - x[0])
    lamb = math.radians(y[1] - x[1])
    a = math.sin(phi/2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(lamb/2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def closestPoint(x, center, method):
    index = -1
    minDist = float("INF")
    for i in range(len(center)):
        if method == "Euclidean":
            distance = Euclidean(x, center[i])
        else:
            distance = GreatCircle(x, center[i])
        if distance < minDist:
            minDist = distance
            index = i
    return index

def addPoints(x, y):
    return (x[0] + y[0], x[1] + y[1], x[2] + y[2])



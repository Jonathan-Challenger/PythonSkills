"""
This problem takes two inputs of integer arrays. One is points on a graph. The other is 
the centre point of a circle and its radius. We should return the number of points inside
each of the circles on the graph. Points on the edge of the circle are included as inside.
"""

queries = [[2,3,1],[4,3,1],[1,1,2]]

points = [[1,3],[3,3],[5,3],[2,2]]

def countPoints(points, queries):
    ans = []
    for i, j, r in queries:
        res = 0
        for x, y in points:
            d = ((i - x)**2 + (j - y)**2) ** 0.5
            if d <= r:
                res += 1
        ans.append(res)
    return ans


print(countPoints(points, queries))


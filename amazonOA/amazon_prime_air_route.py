'''
Given a list of forward air routes and backward air routes,
and a maximum distance, return pairs of optimal routes such that
the sum of forward distance and backward distance is just less than
or equal to the optimal distance.

example
--------
max distance: 11000
forward route: [[1, 3000], [2, 5000], [3, 4000], [4, 10000]]
backward route: [[1, 2000], [2, 3000], [3, 4000]]

ans: (2, 3)
'''

def optimal_air_route(forward_routes, backward_routes, optimal_dist):
    '''
    The idea is to sort forward routes, and for each backward route,
    we find the optimal forward route (such that the forward_dist + backward_dist <= optimal_dist)
     for that route using binary search on forward routes.

    Time complexity - NlogN (for sorting forward routes) + MlogN(for binary search)
    '''
    forward_routes = sorted(forward_routes, key=lambda x: x[1])
    result = [0, 0, 0]
    for route_id, dist in backward_routes:
        i = 0
        j = len(forward_routes)
        target = optimal_dist - dist
        while i < j:
            mid = (i + j) // 2
            val = forward_routes[mid][1]
            if target == val:
                result = [forward_routes[mid][0], route_id, val]
                return result[:2]
            elif val > target:
                j = mid - 1
            else:
                i = mid
        
        total_dist = forward_routes[i][1] + dist
        if total_dist > result[2]:
            result = [forward_routes[i][0], route_id, total_dist]

    return result[:2]

f = [[1, 3000], [2, 5000], [3, 4000], [4, 10000]]
b = [[1, 2000], [2, 3000], [3, 4000]]
d = 11000

print(optimal_air_route(f, b, d))

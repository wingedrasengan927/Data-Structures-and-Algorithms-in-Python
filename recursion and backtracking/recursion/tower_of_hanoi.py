'''
Problem Statement: https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/tower-of-hanoi-17/
Basically we have three towers: source, destination, auxillary
Our aim is to move all the disks from source to destination with some rules:
1. You can only move one disk at a time
2. Larger disk cannot be placed on top of a smaller disk

Solution
--------
1. Move the top n-1 disks from source to auxillary tower
2. Move the nth disk from source to destination
3. Move the n-1 disks from auxillary to destination tower
'''

def move_tower(ndisks, fromTower, toTower, withTower):
    # time complexity - 2^n - 1
    if ndisks >= 1:
        move_tower(ndisks-1, fromTower, withTower, toTower)
        move_disk(fromTower, toTower)
        move_tower(ndisks-1, withTower, toTower, fromTower)


def move_disk(fromTower, toTower):
    print("Moving disk from {} tower to {} tower".format(fromTower, toTower))

move_tower(3, "source", "destination", "auxillary")
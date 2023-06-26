import pyautogui as pi
import math
import numpy as np
from scipy.spatial import KDTree
import time

def calculate_distance(point1, point2):
    distance = np.linalg.norm(np.array(point2) - np.array(point1))
    return distance

def find_nearest_pointN(target_point, points):
    nearest_point = None
    min_distance = float('inf')  # Initialize with a large value

    for point in points:
        distance = calculate_distance(target_point, point)
        if distance < min_distance:
            min_distance = distance
            nearest_point = point

    return nearest_point


def find_nearest_pointT(target_point, points):
    kdtree = KDTree(points)
    _, nearest_idx = kdtree.query(target_point)
    nearest_point = points[nearest_idx]
    return nearest_point


target_point = (3, 4)
points = [
    (1, 2),
    (3, 4),
    (5, 6),
    (7, 8),
    (9, 10),
    (11, 12),
    (13, 14),
    (15, 16),
    (17, 18),
    (19, 20),
    (21, 22),
    (23, 24),
    (25, 26),
    (27, 28),
    (29, 30),
    (31, 32),
    (33, 34),
    (35, 36),
    (37, 38),
    (39, 40),
    (41, 42),
    (43, 44),
    (45, 46),
    (47, 48),
    (49, 50),
    (51, 52),
    (53, 54),
    (55, 56),
    (57, 58),
    (59, 60),
    (61, 62),
    (63, 64),
    (65, 66),
    (67, 68),
    (69, 70),
    (71, 72),
    (73, 74)
]

start_time = time.time()
nearest = find_nearest_pointT(target_point, points)
end_time = time.time()
print(f"The nearest point to {target_point} is {nearest}")
elapsed_time = end_time - start_time
print(f"Execution time: {elapsed_time} seconds")

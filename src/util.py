import numpy as np


def perpendicular(v):
    """

    :param v: array of length 2 representing a 2d vector
    :return:
    """
    perp = np.array([-v[1], v[0]])
    return perp


def projection(a, b):
    """
    return the projection of a onto b.
    :param a:
    :param b:
    :return:
    """
    return np.dot(np.dot(a, b), b) / (np.linalg.norm(b) ** 2)  # simple vector projection


def projection_scalar(a, b):
    """
    return the scalar of the projection of a onto b
    :param a:
    :param b:
    :return:
    """
    return np.dot(a, b) / np.linalg.norm(b)


def unit(v):
    """
    Return the unit vector
    :param v: vector for which the unit vector will be returned. must be np.array
    :return: unit vector of v
    """
    return v / np.linalg.norm(v)


def projections(points, b):
    points_projected = []
    for point in points:
        p = np.array(point)
        p_projected = projection(p, b)
        points_projected.append(p_projected)
    return points_projected


def projection_scalars(points, b):
    points_projected_scalars = []
    for point in points:
        p = np.array(point)
        p_projected_scalar = projection_scalar(p, b)
        points_projected_scalars.append(p_projected_scalar)
    return points_projected_scalars


def find_edges(polygon):
    """
    return edges of the polygon
    :param polygon: the polygon for which edges will be found, as a list of vertices
    :return: edges in the form of [(start, end)] where start is the starting vertex, and end is the ending vertex
    """
    vertices = polygon
    next_vertices = vertices[1:] + [vertices[0]]
    edges = list(zip(vertices, next_vertices))
    return edges


def detect_collision(p1, p2):
    """
    detect collision between convex polygons a and b, based on the separating axes theorem
    :param a: a convex polygon, as a list of vertices
    :param b: a convex polygon, as a list of vertices
    :return: if the polygons overlap
    """
    edges = []
    edges.append(find_edges(p1))
    edges.append(find_edges(p2))
    for i in range(len(edges)):
        for edge in edges[i]:
            start = np.array(edge[0])
            end = np.array(edge[1])
            v = end - start
            p = perpendicular(v)  # perpendicular
            projected_scalars = []
            projected_scalars.append(projection_scalars(p1, p))
            projected_scalars.append(projection_scalars(p2, p))
            # now, we have the scalars of all vertex projections onto the perpendicular of the current edge.
            # this means that we can find the max and min of both sets of scalars (a and b), and check if they are disjoint.
            ps_bounds = []
            for ps in projected_scalars:
                ps_bounds.append([min(ps), max(ps)])
            a, b = ps_bounds[0]
            c, d = ps_bounds[1]
            if (a < c and b < c) or (b > d and a > d):
                return False
    return True


if __name__ == '__main__':
    square1 = np.array([[1, 3], [3, 3], [3, 1], [1, 1]])
    square2 = np.array([v + [1,1] for v in square1])
    square3 = np.array([v + [1,1] for v in square2])
    square4 = np.array([v + [1,1] for v in square3])
    print(detect_collision(square1, square2))
    print(detect_collision(square1, square3))
    print(detect_collision(square1, square4))
    # print(detect_collision([[1,3],[3,3]]))
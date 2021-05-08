import numpy as np

def perpendicular(v):
    """

    :param v: array of length 2 representing a 2d vector
    :return:
    """
    perp = np.array([-v[1], v[0]])
    return perp


def project(a, b):
    """
    return the projection of a onto b.
    :param a:
    :param b:
    :return:
    """
    return np.dot(np.dot(a,b),b)/(np.linalg.norm(b)**2) # simple vector projection


def unit(v):
    """
    Return the unit vector
    :param v: vector for which the unit vector will be returned. must be np.array
    :return: unit vector of v
    """
    return v/np.linalg.norm(v)


def project_all(points, b):
    points_projected = []
    for point in points:
        p = np.array(p)
        p_projected = project(p,b)
        points_projected.append(p_projected)
    return points_projected

def find_edges(polygon):
    """
    return edges of the polygon
    :param polygon: the polygon for which edges will be found. polygon must be a set of vertices
    :return: edges in the form of [(start, end)] where start is the start coordinates of the edge, and end is the end coordinates of the edge.
    """
    vertices = polygon
    next_vertices = vertices[1:] + [vertices[0]]
    edges = list(zip(vertices, next_vertices))
    return edges

def detect_collision(a,b):
    """
    detect collision between convex polygons a and b, based on the separating axes theorem
    :param a: a convex polygon
    :param b: a convex polygon
    :return: if the polygons overlap
    """
    edges = []
    edges.append(find_edges(a))
    edges.append(find_edges(b))
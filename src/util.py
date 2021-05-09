import numpy as np
import math


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
    next_vertices = np.append(vertices[1:], [vertices[0]], axis=0)
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


def detect_collision_pairs(ps1, ps2):
    """
    detect collision between two lists of convex polygons.
    :param ps1: first list of convex polygons
    :param ps2: second list of convex polygons
    :return: all pairs of (p1,p2) that collide where p1 in ps1 and p2 in ps2
    """
    pairs = []
    perps = [{},{}]
    for i in range(len(ps1)):
        p1 = ps1[i]
        ps = []
        edges = find_edges(p1)
        for e in edges:
            start = np.array(e[0])
            end = np.array(e[1])
            ps.append(perpendicular(end - start))
        perps[0][i] = ps
    for j in range(len(ps2)):
        p2 = ps2[j]
        ps = []
        edges = find_edges(p2)
        for e in edges:
            start = np.array(e[0])
            end = np.array(e[1])
            ps.append(perpendicular(end - start))
        perps[1][j] = ps
    for i in range(len(ps1)):
        p1 = ps1[i]
        # todo: dynamically store bounds of projection scalars of vertices onto perpendiculars.
        # p1_scalars = []
        # for p in ps1_perps[p1]: # perpendicular
        #     p1_scalars.append(projection_scalars(p1, p))
        for j in range(len(ps2)):
            p2 = ps2[j]
            no_collision = False
            for p in [x for x in perps[0][i] or x in perps[1][j]]:
                scalars = []
                scalars.append(projection_scalars(p1, p))
                scalars.append(projection_scalars(p2, p))
                bounds = []
                for s in scalars:
                    bounds.append([min(s), max(s)])
                a, b = bounds[0]  # p1
                c, d = bounds[1]  # p2
                if (a < c and b < c) or (b > d and a > d):
                    no_collision = True
                    break
            if no_collision:
                continue
            pairs.append((i, j))
    return pairs


def rotate_in_direction(v, dir):
    rot_mat = np.dot(dir, np.array([[[0, 1], [1, 0]], [[-1, 0], [0, 1]]]))
    return np.dot(rot_mat, v)


def direction(angle):
    a = angle / 360 * 2 * math.pi
    return [math.sin(a), math.cos(a)]


if __name__ == '__main__':
    square1 = np.array([[1, 3], [3, 3], [3, 1], [1, 1]])
    square2 = np.array([v + [1, 1] for v in square1])
    square3 = np.array([v + [1, 1] for v in square2])
    square4 = np.array([v + [1, 1] for v in square3])
    print(detect_collision(square1, square2))
    print(detect_collision(square1, square3))
    print(detect_collision(square1, square4))
    # print(detect_collision([[1,3],[3,3]]))

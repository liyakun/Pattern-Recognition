import random
import numpy as np
from collections import namedtuple
from operator import itemgetter
from pprint import pformat
import matplotlib.pyplot as plt

class Node(namedtuple('Node', 'location left_child right_child')):
    def __repr__(self):
        return pformat(tuple(self))

# line width for visualization of K-D tree
line_width = [4., 3.5, 3., 2.5, 2., 1.5, 1., .5, 0.3]

def plot_tree(tree, min_x, max_x, min_y, max_y, prev_node, branch, depth=0):
    """ plot K-D tree
    :param tree      input tree to be plotted
    :param min_x
    :param max_x
    :param min_y
    :param max_y
    :param prev_node parent's node
    :param branch    True if left, False if right
    :param depth     tree's depth
    :return tree     node
    """

    cur_node = tree.location         # current tree's node
    left_branch = tree.left_child    # its left branch
    right_branch = tree.right_child  # its right branch

    # set line's width depending on tree's depth
    if depth > len(line_width)-1:
        ln_width = line_width[len(line_width)-1]
    else:
        ln_width = line_width[depth]

    k = len(cur_node)
    axis = depth % k

    # draw a vertical splitting line
    if axis == 0:

        if branch is not None and prev_node is not None:

            if branch:
                max_y = prev_node[1]
            else:
                min_y = prev_node[1]

        plt.plot([cur_node[0],cur_node[0]], [min_y,max_y], linestyle='-', color='red', linewidth=ln_width)

    # draw a horizontal splitting line
    elif axis == 1:

        if branch is not None and prev_node is not None:

            if branch:
                max_x = prev_node[0]
            else:
                min_x = prev_node[0]

        plt.plot([min_x,max_x], [cur_node[1],cur_node[1]], linestyle='-', color='blue', linewidth=ln_width)

    # draw the current node
    plt.plot(cur_node[0], cur_node[1], 'ko')

    # draw left and right branches of the current node
    if left_branch is not None:
        plot_tree(left_branch, min_x, max_x, min_y, max_y, cur_node, True, depth+1)

    if right_branch is not None:
        plot_tree(right_branch, min_x, max_x, min_y, max_y, cur_node, False, depth+1)

def get_data_list():
    dt = np.dtype([('x1', np.float), ('x2', np.float), ('y',  np.float)])
    data = np.loadtxt('./data2-train.dat', dtype=dt, comments='#', delimiter=None)
    Xtr,ytr = np.array([[el[0],el[1]] for el in data]),data['y']
    nested_lst_of_tuples = [tuple(l) for l in Xtr]
    return nested_lst_of_tuples

def generate_point_list(n, min_val, max_val):
    """ generate a list of random points
    :param n        number of points
    :param min_val  minimal value
    :return max_val maximal value
    """

    p = []

    for i in range(n):

        # coordinates as integer values
        p.append((random.randint(min_val,max_val),
                  random.randint(min_val,max_val)))

        # coordinates as float values
        #p.append((np.random.normal(random.randint(min_val,max_val), scale=0.5),
        #          np.random.normal(random.randint(min_val,max_val), scale=0.5)))
    print p
    return p

def kdtree(point_list, depth=0):
    try:
        k = len(point_list[0]) # assumes all points have the same dimension
    except IndexError as e: # if not point_list:
        return None
    # Select axis based on depth so that axis cycles through all valid values
    axis = depth % k

    # Sort point list and choose median as pivot element
    point_list.sort(key=itemgetter(axis))
    median = len(point_list) // 2 # choose median

    # Create node and construct subtrees
    return Node(
        location=point_list[median],
        left_child=kdtree(point_list[:median], depth + 1),
        right_child=kdtree(point_list[median + 1:], depth + 1)
    )

def main():
    """Example usage"""
    #min_val = 100
    #max_val = 300
    delta = 1
    #point_list = generate_point_list(100, 0, 50)
    point_list = get_data_list()
    max_val = int(max(map(max, zip(*point_list))))
    min_val = int(min(map(min, zip(*point_list))))
    tree = kdtree(point_list)

    plt.figure("K-d Tree", figsize=(10., 10.))
    plt.axis( [min_val-delta, max_val+delta, min_val-delta, max_val+delta] )

    plt.grid(b=True, which='major', color='0.75', linestyle='--')
    plt.xticks([i for i in range(min_val-delta, max_val+delta, 1)])
    plt.yticks([i for i in range(min_val-delta, max_val+delta, 1)])

    # draw the tree
    plot_tree(tree, min_val-delta, max_val+delta, min_val-delta, max_val+delta, None, None)

    plt.title('K-D Tree')
    plt.show()
    plt.close()

if __name__ == '__main__':
    main()
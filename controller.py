### Beatz CONTROLLER

"""
Controller handles collisions as well as user input actions.
"""

class Collisions():
    def __init__(self, pos, size):
        self.x = pos[0]
        self.y = pos[1]
        self.width = size[0]
        self.height = size[1]


def collisions(point, element, tolerance = 0):
    """ 
    Check to see if the center point is colliding/within the range of the element.
    """

    # for point.x in xrange(element.x + element.width):
        # return

    return (point.x >= element.x) and (point.x <= (element.x + element.width)) and (point.y >= element.y) and (point.y <= (element.y + element.height))

    # return ((((element2.x) - (point.x + point.width) + tolerance) * ((element2.x) - (point.x) + tolerance)) <= 0 \
    #     or (((point.x) - (element2.x + element2.width) + tolerance) * ((point.x + point.width) - (element2.x + element2.width) + tolerance)) <= 0) \
    #     and ((((element2.y) - (point.y + point.height) + tolerance) * ((element2.y) - (point.y) + tolerance)) <= 0 \
    #     or (((point.y) - (element2.y + element2.height) + tolerance) * ((point.y + point.height) - (element2.y + element2.height) + tolerance)) <= 0)


if __name__ == "__main__":
    collisions()
### Beatz MODEL
""" 
Define classes and inheritance for instruments.
"""

class Instrument(object):
    """
    Parent class for instruments: Drum and Hat. 
    Defined attributes: x position, y position, object width, and object height. 
    Defined methods: load_image, load_sound
    """

    def __init__(self, pos, size, imgPath, sndPath):    # Note: pos and size are tuples.
        self.x = pos[0]
        self.y = pos[1]
        self.width = size[0]
        self.height = size[1]
        self.imgPath = imgPath

    def __str__(self):
        pass


"""
Child classes of the parent class Instrument
"""
class Drum(Instrument):
    def 
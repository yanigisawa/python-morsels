class Point(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y}, z={self.z})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __add__(self, other):
        return Point(x=self.x + other.x, y=self.y + other.y, z=self.z + other.z)

    def __sub__(self, other):
        return Point(x=self.x - other.x, y=self.y - other.y, z=self.z - other.z)

    def __mul__(self, term):
        return Point(x=self.x * term, y=self.y * term, z=self.z * term)

    def __rmul__(self, term):
        return Point(x=self.x * term, y=self.y * term, z=self.z * term)

    def __iter__(self):
        return iter((self.x, self.y, self.z))


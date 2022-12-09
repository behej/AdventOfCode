#! /usr/bin/python3

class Knot:
    def __init__(self):
        self.__x = 0
        self.__y = 0
        self.__next = None
        self.__parent = None

    def __repr__(self):
        """Display coordinates."""
        return "({}, {})".format(self.__x, self.__y)

    def add_knot(self):
        """Create an attached knot."""
        self.__next = Knot()
        self.__next.__parent = self

    def next(self):
        """Return attached knot."""
        return self.__next

    def coord(self):
        """Return coordinates tuple."""
        return (self.__x, self.__y)

    def move(self, dir):
        """Move knot into any direction (L, R, U, D).
        Attached knot (if present) tries to follow.
        """
        if dir == 'L':
            self.__x -= 1
        elif dir == 'R':
            self.__x += 1
        elif dir == 'U':
            self.__y += 1
        elif dir == 'D':
            self.__y -= 1

        if self.__next:
            self.__next.follow()

    def follow(self):
        """Follow parent knot.
        If parent is close enough, nothing to move, return directly.
        If parent is to far, move this knot towards parent and make attached knot follow.
        """
        if (self.__parent.__x - 1 <= self.__x <= self.__parent.__x + 1) and \
            (self.__parent.__y - 1 <= self.__y <= self.__parent.__y + 1):
            # No move
            pass
        else:
            # move
            if (self.__parent.__y > self.__y):
                self.__y += 1
            if (self.__parent.__y < self.__y):
                self.__y -= 1
            if (self.__parent.__x  > self.__x):
                self.__x += 1
            if (self.__parent.__x < self.__x):
                self.__x -= 1

            if self.__next:
                self.__next.follow()




def register_tail():
    if tail.coord() not in visited:
        visited.append(tail.coord())



visited = []
head = Knot()

k = head
for i in range(9):
    k.add_knot()
    k = k.next()
tail = k



with open("input", "r") as f:
    for l in f:
        for i in range(int(l.split()[1])):
            head.move(l.split()[0])
            register_tail()


print(len(visited))

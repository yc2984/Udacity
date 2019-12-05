class Rod:
    def __init__(self, name, arr=[]):
        self.name = name
        self.arr = arr

    def append(self, value):
        self.arr.append(value)

    def pop(self):
        if self.size() == 0:
            return None
        return self.arr.pop()

    def size(self):
        return len(self.arr)


def tower_of_Hanoi(num_disks):
    """
    :param: num_disks - number of disks
    TODO: print the steps required to move all disks from source to destination
    """
    source_rod = Rod(name="S", arr=list(range(num_disks)))  # num_disks = 2, then source_rod = [0, 1]
    aux_rod = Rod("A")
    des_rod = Rod("D")

    def _move_one_step(from_rod, to_rod):
        value = from_rod.pop()
        to_rod.append(value)
        print("{} {}".format(from_rod.name, to_rod.name))

    def _move_disks(from_rod, to_rod, mid_rod, number_of_disks):
        """This function moves 2 disks from from_rod to to_rod with the help of mid_rod
        """
        if number_of_disks == 0:
            return

        if number_of_disks == 1:
            _move_one_step(from_rod, to_rod)
            return

        _move_disks(from_rod, mid_rod, to_rod, number_of_disks - 1)
        _move_one_step(from_rod, to_rod)
        _move_disks(mid_rod, to_rod, from_rod, number_of_disks - 1)

    _move_disks(source_rod, des_rod, aux_rod, num_disks)


tower_of_Hanoi(3)

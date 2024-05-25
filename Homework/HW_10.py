"""Файл 29  № 4, 6, 7, 14"""

class BinTree:
    def __init__(self, data = None, left = None, right = None) -> None:
        self._data = data
        self._left = left
        self._right = right

    def __repr__(self) -> str:
        return f'{self._data = }, {self._left = }, {self._right = }'

    @property
    def left(self):
        return self._left
    @property
    def right(self):
        return self._right
    #???????????????????????????????????
    def __len__(self):
        if self.left is not None:
            self.left.__len__()
        if self.right is not None:
            self.right.__len__()
        


obj = BinTree(2, left = BinTree(1), right = BinTree(10))
print(obj.right)


#29.13
twenty_nine_13_1 = BinTree(1,
                            left = BinTree(2,
                                           left = BinTree(4), 
                                           right = BinTree(5)), 
                            right = BinTree(3, 
                                            left = BinTree(6)))
twenty_nine_13_2 = BinTree(1,
                            left = BinTree(2,
                                           left = BinTree(4), 
                                           right = BinTree(5)), 
                            right = BinTree(3, 
                                            left = BinTree(6), 
                                            right = BinTree(7)))

#29.14
twenty_nine_14_1 = BinTree(4,
                            left = BinTree(3,
                                           left = BinTree(1),
                                           right = BinTree(2)),
                            right = BinTree(7, 
                                            left = BinTree(6),
                                            right = BinTree(9)))
twenty_nine_14_2 = BinTree(1,
                            left = BinTree(1,
                                            right = BinTree(3,
                                                            left = BinTree(2))))
twenty_nine_14_3 = BinTree(4,
                            left = BinTree(1,
                                            right = BinTree(3,
                                                            left = BinTree(2))))


print(len(twenty_nine_14_2))
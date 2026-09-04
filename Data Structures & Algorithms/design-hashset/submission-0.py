class MyHashSet:

    def __init__(self):
        self.elementos = []

    def add(self, key: int) -> None:
        if key not in self.elementos:
            self.elementos.append(key)
        

    def remove(self, key: int) -> None:
        if key in self.elementos:
            self.elementos.remove(key)
        

    def contains(self, key: int) -> bool:
        if key in self.elementos:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
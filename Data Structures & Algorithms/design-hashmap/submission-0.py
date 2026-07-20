class ListNode:
    def __init__(self, key=-1, value=-1, next_node=None):
        self.key = key
        self.value = value
        self.next = next_node


class MyHashMap:

    def __init__(self):

        self.buckets = [ListNode() for _ in range(1000)]

    def _hash(self, key: int) -> int:
        return key % len(self.buckets)

    def put(self, key: int, value: int) -> None:
        current = self.buckets[self._hash(key)]

        while current.next:
            if current.next.key == key:
                current.next.value = value
                return

            current = current.next

        current.next = ListNode(key, value)

    def get(self, key: int) -> int:

        current = self.buckets[self._hash(key)].next

        while current:
            if current.key == key:
                return current.value

            current = current.next

        return -1

    def remove(self, key: int) -> None:
        current = self.buckets[self._hash(key)]

        while current.next:
            if current.next.key == key:
                current.next = current.next.next
                return

            current = current.next


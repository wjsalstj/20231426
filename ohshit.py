import csv

class BidirectNode:
    def __init__(self, item, prev, next):
        self.item = item
        self.prev = prev
        self.next = next


class Friend:
    def __init__(self, name, birth):  # birth: yyyymmdd 형식
        self.name = name
        self.birth = birth

    def __repr__(self):
        return f"{self.name} ({self.birth})"


same_team = {
    "이원진", "박찬미", "박혜린", "임서영",
    "이서현", "안소민", "이채민", "이예림",
    "이수빈", "김효리", "이지영", "이진", "김나림", "이가연"
}


class CircularDoublyLinkedList:
    def __init__(self):
        self.__head = BidirectNode("dummy", None, None)
        self.__head.prev = self.__head
        self.__head.next = self.__head
        self.__numItems = 0

    def append(self, newItem) -> None:
        prev = self.__head.prev
        newNode = BidirectNode(newItem, prev, self.__head)
        prev.next = newNode
        self.__head.prev = newNode
        self.__numItems += 1

    def __iter__(self):
        return CircularDoublyLinkedListIterator(self)

    def getNode(self, i: int) -> BidirectNode:
        curr = self.__head
        for _ in range(i + 1):
            curr = curr.next
        return curr

class CircularDoublyLinkedListIterator:
    def __init__(self, alist):
        self.__head = alist.getNode(-1)
        self.iterPosition = self.__head.next

    def __next__(self):
        if self.iterPosition == self.__head:
            raise StopIteration
        else:
            item = self.iterPosition.item
            self.iterPosition = self.iterPosition.next
            return item

    def __iter__(self):
        return self


friend_list = CircularDoublyLinkedList()


with open("D:/성신여대/2025 1학기/자료구조/6주차/birthday.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        name = row['이름'].strip()
        birth = row['생년월일8자리(예.20040101)'].strip()

        if not birth.isdigit():
            continue

        friend = Friend(name, birth)
        friend_list.append(friend)


print("같은 조 친구들의 이름 - 생일:")
for friend in friend_list:
    if friend.name in same_team:
        print(f"{friend.name} - {friend.birth}")

"""d"""
class  SinglyLinkedList:
    """g"""
    def __init__(self, count=0, head=None):
        """f"""
        self.count = count
        self.head = head
        self.item = []

    def traverse(self):
        """f"""
        check = self.count
        if self.item == []:
            print("This is an empty list.")
        else:
            for i in self.item:
                print(i, end="")
                if check > 1:
                    print(" -> ", end="")
                check -= 1

    def insert_last(self, data):
        """F"""
        self.item.append(data)
        self.count += 1

def main():
    mylist = SinglyLinkedList()
    for _ in range(int(input())):
        mylist.insert_last(input())
    mylist.traverse()
main()

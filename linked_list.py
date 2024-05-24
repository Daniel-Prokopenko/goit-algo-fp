class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def reverse(self):
        prev = None
        cur = self.head
        while cur is not None:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        self.head = prev

    def merge_sort(self):
        if self.head is None or self.head.next is None:
            return self.head
        middle = self.get_middle(self.head)
        next_to_middle = middle.next
        middle.next = None
        left = LinkedList()
        right = LinkedList()
        left.head = self.head
        right.head = next_to_middle
        left.head = left.merge_sort()
        right.head = right.merge_sort()
        self.head = self.sorted_merge(left.head, right.head)
        return self.head

    def get_middle(self, head):
        if head is None:
            return head
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def sorted_merge(self, left, right):
        if left is None:
            return right
        if right is None:
            return left
        if left.data <= right.data:
            result = left
            result.next = self.sorted_merge(left.next, right)
        else:
            result = right
            result.next = self.sorted_merge(left, right.next)
        return result


def merge(first, second):
    if first is None:
        return second
    if second is None:
        return first
    if first.data <= second.data:
        result = first
        result.next = merge(first.next, second)
    else:
        result = second
        result.next = merge(first, second.next)
    return result


my_list = LinkedList()


my_list.insert_at_beginning(3)
my_list.insert_at_beginning(2)
my_list.insert_at_beginning(1)


print("Список після вставки в початок:")
my_list.print_list()

my_list.insert_at_end(4)
my_list.insert_at_end(5)


print("\nСписок після вставки в кінець:")
my_list.print_list()


node_to_insert_after = my_list.search_element(3)
if node_to_insert_after:
    my_list.insert_after(node_to_insert_after, 3.5)


print("\nСписок після вставки після 3:")
my_list.print_list()


my_list.delete_node(3.5)


print("\nСписок після видалення 3.5:")
my_list.print_list()


search_result = my_list.search_element(4)
if search_result:
    print("\nЭлемент знайдено:", search_result.data)
else:
    print("\nЭлемент не знайдено")


print("\nРозвернутий список:")
my_list.reverse()
my_list.print_list()


print("\nСписок після сортування злиттям:")
my_list.merge_sort()
my_list.print_list()


list1 = LinkedList()
list1.insert_at_end(1)
list1.insert_at_end(3)
list1.insert_at_end(5)


list2 = LinkedList()
list2.insert_at_end(2)
list2.insert_at_end(4)
list2.insert_at_end(6)


merged_list = merge(list1.head, list2.head)


print("Результат злиття двох відсортованих списків:")
current = merged_list
while current:
    print(current.data)
    current = current.next

def parse_input(path):
    rules = {}
    with open(path) as f:
        for idx, line in enumerate(f):
            if idx == 0:
                template = line.strip()
            elif idx >= 2:
                pair, insert = line.strip().split(' -> ')
                rules[pair] = insert
    return template, rules

# Array method
def calc_pt1_arrays(template, rules):
    polymer = list(template)

    for step in range(10):
        print(step)
        new_polymer = polymer.copy()
        num_inserted = 0

        for i in range(len(polymer)-1):
            pair = polymer[i:i+2]
            pair_str = ''.join(pair)
            if pair_str in rules:
                new_polymer.insert(i + 1 + num_inserted, rules[pair_str])
                num_inserted += 1
        polymer = new_polymer

    most, least = most_least_common(polymer)
    print(most, least)
    return most - least

# Linked List method
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_end(self, val):
        if self.head is None:
            self.head = Node(val)
            return
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = Node(val)

    def to_array(self):
        arr = []
        curr = self.head
        while curr is not None:
            arr.append(curr.data)
            curr = curr.next
        return arr

    def __str__(self):
        string = ''
        curr = self.head
        while curr is not None:
            string += curr.data
            curr = curr.next
        return string

def create_linked_list(str):
    ll = LinkedList()
    for char in str:
        ll.insert_end(char)
    return ll

def copy_linked_list(linked_list):
    new_ll = LinkedList()
    curr = linked_list.head
    while curr.next is not None:
        new_ll.insert_end(curr.data)
        curr = curr.next
    new_ll.insert_end(curr.data)
    return new_ll

def calc_pt1_linked_list(template, rules):
    polymer = create_linked_list(template)

    for step in range(10):
        new_polymer = copy_linked_list(polymer)

        curr = new_polymer.head
        while curr.next is not None:
            pair = curr.data + curr.next.data
            if pair in rules:
                # Insert node
                new_node = Node(rules[pair])
                new_node.next = curr.next
                curr.next = new_node
                # Move one forward
                curr = curr.next

            curr = curr.next
        polymer = new_polymer

    most, least = most_least_common(polymer.to_array())
    print(most, least)
    return most - least

# Helper
def most_least_common(polymer):
    counts = {}
    for elem in polymer:
        if elem in counts:
            counts[elem] += 1
        else:
            counts[elem] = 1
    return max(counts.values()), min(counts.values())


template, rules = parse_input('input.txt')
result = calc_pt1_linked_list(template, rules)
print(result)
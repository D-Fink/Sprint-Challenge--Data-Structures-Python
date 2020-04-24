from doubly_linked_list import DoublyLinkedList

# We would want to use a linked list for its easy insertion/deletion and
# also allows us to easily keep track of our MRU and LRU

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    # Make a Queue to push out LRU values with new/MRU values as capacity reached
    def append(self, item):
        # if not at capacity...
        if len(self.storage) < self.capacity:
            # add to most recent
            self.storage.add_to_tail(item)
        else:
            # if at the end or next node is the end...
            if self.current == None or self.current.next == None:
                # set current to last used for replacement
                self.current = self.storage.head
            # otherwise just go to the next of current val
            else:
                self.current = self.current.next
            # replace our current val with item
            self.current.value = item


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        # set node to head
        node = self.storage.head
        # until we reach the end...
        while node != None:
            # add item values to list
            list_buffer_contents.append(node.value)
            # move to next
            node = node.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass

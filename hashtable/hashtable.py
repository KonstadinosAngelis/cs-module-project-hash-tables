class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    Implement this.
    """
    def __init__(self, capacity):
        self.capacity = [None] * MIN_CAPACITY
        self.length = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.capacity)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        #number of things stored in the has table / number of slots in the array
        return self.length // self.get_num_slots()

    def djb2(self, key):
        hash = 5381

        for x in key:
            hash = (( hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFF


    def hash_index(self, key):
        return self.djb2(key) % len(self.capacity)


    def put(self, key, value):
        slot = self.hash_index(key)

        if self.capacity[slot] is not None:
            if self.capacity[slot].value is not None:
                cur = self.capacity[slot]
                self.capacity[slot] = HashTableEntry(key, value)
                self.capacity[slot].next = cur

                # increment length
                self.length += 1

                #check for load size
                if self.get_load_factor() >= 0.7:
                    self.resize(MIN_CAPACITY * 2)
                return

        self.capacity[slot] = HashTableEntry(key, value)
        # increment length
        self.length += 1

        #check for load size
        if self.get_load_factor() >= 0.7:
            self.resize(MIN_CAPACITY * 2)


    def delete(self, key):
        self.put(key, None)
        self.length -= 1


    def get(self, key):
        slot = self.hash_index(key)
        hash_entry = self.capacity[slot]

        if hash_entry is not None:
            while hash_entry.next is not None:
                if hash_entry.key == key:
                    return hash_entry.value
                hash_entry = hash_entry.next

            return hash_entry.value
        
        return None


    def resize(self, new_capacity):
        global MIN_CAPACITY
        MIN_CAPACITY = new_capacity

        cur = self.capacity

        self.capacity = [None] * MIN_CAPACITY
        
        for e in cur:
            if(e is not None):
                if (e.next is not None):
                    pointer = e.next
                    while pointer is not None:
                        self.put(pointer.key, pointer.value)
                        pointer = e.next
                self.put(e.key, e.value)



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    ht.get_load_factor()

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")

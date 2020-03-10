# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.size = 0
        self.keys = []


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        if key in self.keys:
            raise KeyError("Key has already been used")

        #create the index by hashing the key
        index = self._hash_mod(key)
        # determine whether this is the first entry or not
        if self.size == 0:
            self.storage[index] = LinkedPair(key,value)
        # The table is populated
        elif self.size > 0:
            # if the index is available
            if self.storage[index] is None:
                self.storage[index] = LinkedPair(key,value)
            # if theres already a value there
            else:
                print("collision")
                while self.storage[index] is not None:
                    self.storage[index].next = LinkedPair(key,value)
                    self.storage[index] = self.storage[index].next

        self.keys.append(key)


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        
        index = self._hash_mod(key)
        node = self.storage[index]
        

        if key not in self.keys:
            return f"The key '{key}' is not in the Table"
        else:            
            # if theres only one node at the index set the index value back to none
            if node.next is None:
                self.storage[index] = None
            
            else:
                while node is not None:
                    if node.key == key:
                        new_head = node.next
                        del node
                        self.storage[index] = new_head
                    elif node.next.key == key:
                        nex = node.next.next
                        del node.next
                        node.next = nex
                    else:
                        node = node.next

        self.size -= 1
        

    def buckets(self):
        for count,node in enumerate(self.storage):
            print(f"Bucket #{count+1}")
            while node is not None:
                print(f"{node.key}: {node.value}")
                node = node.next
            print()
            

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # get the index of a given key
        # when the index is found 
        # look at each node in the bucket for the key
        # when the key is found return the value
        index = self._hash_mod(key)
        node = self.storage[index]

        if key not in self.keys:
            return f"The key '{key}' is not in the Table"
        else:
            while node is not None:
                if key == node.key:
                    return node.value
                
                node = node.next
            


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        
        # double the capacity by multiplying self.capacity by 2
        self.capacity *= 2
        # reassign self.storage to [None] * capacity
        new_storage = [None] * self.capacity
        # loop over old storage and call insert on ith key and  value
        for i in range(len(self.storage)):
            new_storage[i] = self.storage[i]
        
        self.storage = new_storage
        return f"Resized table to {self.capacity}"



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")


'''table = HashTable(5)
table.insert("one",1)
table.insert("two",2)
table.insert("three",3)
table.insert("four",4)
table.insert("five",5)
#print(table.retrieve("four"))
table.buckets()'''

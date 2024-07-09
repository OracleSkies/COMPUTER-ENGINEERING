class HashMap:
    def __init__(self, size=10):
        # Initialize the hash map with a specified size (default is 10).
        # 'table' is a list of empty lists, each serving as a bucket.
        self.size = size
        self.table = [[] for _ in range(size)]
        self.count = 0  # Initialize the count of key-value pairs to zero.

    def _hash_function(self, key):
        # Private method to compute the hash index for a given key.
        return hash(key) % self.size

    def insert(self, key, value):
        # Insert a key-value pair into the hash map.
        index = self._hash_function(key)  # Compute the index using the hash function.
        for kvp in self.table[index]:  # Check if the key already exists in the bucket.
            if kvp[0] == key:
                kvp[1] = value  # If key exists, update the value.
                return
        self.table[index].append([key, value])  # If key doesn't exist, add the new key-value pair.
        self.count += 1  # Increment the count of key-value pairs.

    def get(self, key):
        # Retrieve the value associated with a given key.
        index = self._hash_function(key)  # Compute the index using the hash function.
        for kvp in self.table[index]:  # Iterate over the bucket to find the key.
            if kvp[0] == key:
                return kvp[1]  # Return the value if key is found.
        return None  # Return None if key is not found.

    def remove(self, key):
        # Remove a key-value pair from the hash map.
        index = self._hash_function(key)  # Compute the index using the hash function.
        for i, kvp in enumerate(self.table[index]):  # Iterate over the bucket to find the key.
            if kvp[0] == key:
                del self.table[index][i]  # Delete the key-value pair if key is found.
                self.count -= 1  # Decrement the count of key-value pairs.
                return

    def contains_key(self, key):
        # Check if a given key exists in the hash map.
        return self.get(key) is not None

    def contains_value(self, value):
        # Check if a given value exists in the hash map.
        for bucket in self.table:  # Iterate over all buckets.
            for kvp in bucket:  # Iterate over all key-value pairs in each bucket.
                if kvp[1] == value:
                    return True  # Return True if value is found.
        return False  # Return False if value is not found.

    def get_size(self):
        # Get the number of key-value pairs in the hash map.
        return self.count

    def is_empty(self):
        # Check if the hash map is empty.
        return self.count == 0

    def keys(self):
        # Retrieve all keys in the hash map.
        keys = []
        for bucket in self.table:  # Iterate over all buckets.
            for kvp in bucket:  # Iterate over all key-value pairs in each bucket.
                keys.append(kvp[0])  # Add each key to the list.
        return keys

    def values(self):
        # Retrieve all values in the hash map.
        values = []
        for bucket in self.table:  # Iterate over all buckets.
            for kvp in bucket:  # Iterate over all key-value pairs in each bucket.
                values.append(kvp[1])  # Add each value to the list.
        return values

    def items(self):
        # Retrieve all key-value pairs in the hash map.
        items = []
        for bucket in self.table:  # Iterate over all buckets.
            for kvp in bucket:  # Iterate over all key-value pairs in each bucket.
                items.append((kvp[0], kvp[1]))  # Add each key-value pair to the list.
        return items

    def clear(self):
        # Remove all key-value pairs from the hash map.
        self.table = [[] for _ in range(self.size)]  # Reset the table to empty buckets.
        self.count = 0  # Reset the count of key-value pairs.

    def __str__(self):
        # Return a string representation of the hash map.
        return str(self.table)
    
#===OUTPUT AREA===
hashMap = HashMap()
hashMap.insert("Apple", 1)
hashMap.insert("Banana",2)
hashMap.insert("Orange",3)
hashMap.insert("Grapes",4)
hashMap.insert("Carrot",5)

#print(f"\n{hashMap}\n")
#print(hashMap.get("Orange"))
#print(hashMap.size)
#print(hashMap.get_size())
#print(hashMap.keys())
#print(hashMap.values())
hashMap.remove("Carrot")
print(f"\n{hashMap}\n")
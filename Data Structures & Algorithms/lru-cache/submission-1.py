from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):

        # assign capcaity
        self.max_capacity = capacity

        # initalising map
        self.m = OrderedDict()
        
    def get(self, key: int) -> int:

        if key in self.m:
            # move it to the end becuase it was most recently accessed
            self.m.move_to_end(key)
            return self.m[key]
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:

        # if exist, update the key's value
        if key in self.m:

            # move to the end because it was recenetly accessed to switch
            self.m.move_to_end(key)
            self.m[key] = value

        # else add it in
        else:
            # checking if gonna exceed lenght
            if len(self.m)==self.max_capacity:

                # finding which key was least recently used key
                oldest_key, oldest_value  = self.m.popitem(last=False)
                self.m[key] = value
            else:
                self.m[key] = value
        

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        # for each new node
        # the key is the old Node and the value is the new Node
        # I cant use values as the key as it is possible for multiple nodes to have the same value
        created_dict = {}

        # getting the defaultdict first
        def dfs(old_node):

            # checking if the node is none
            if old_node is None:
                return
            
            if old_node in created_dict:

                # returning the cloned new node
                return created_dict[old_node]
            
            # if it has not been created before, create it now
            created_dict[old_node] = Node(old_node.val)
       
            # for nodes in the neighbours
            for old_neighbour in old_node.neighbors:
                node_to_add = dfs(old_neighbour)
                created_dict[old_node].neighbors.append(node_to_add)
            
            return created_dict[old_node] 
            
        return dfs(node)
                        
        
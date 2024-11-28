from avl import AVLTree 
class Bin:
    def __init__(self, bin_id, capacity):
        self.bin_id=bin_id
        self.capacity=capacity
        self.objects=AVLTree()
        pass

    def add_object(self, object):
        # Implement logic to add an object to this bin
        self.objects.root=self.objects.insert(self.objects.root, object.object_id)
        pass

    def remove_object(self, object_id):
        # Implement logic to remove an object by ID
        self.objects.root=self.objects.delete_node(self.objects.root, object_id)
        pass

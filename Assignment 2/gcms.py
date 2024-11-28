from bin import Bin
from avl import AVLTree
from object import Object, Color
from node import Node
from exceptions import NoBinFoundException
import copy

class GCMS:
    def __init__(self):
        # Maintain all the Bins and Objects in GCMS
        self.bando=AVLTree()
        self.objavl=AVLTree()
        self.binavl=AVLTree()
        pass 

    def add_bin(self, bin_id, capacity):
        key = [capacity, bin_id]  # Tuple (capacity, bin_id)
        binclass=Bin(bin_id,capacity)
        self.bando.root = self.bando.insert(self.bando.root,key)
        self.binavl.root=self.binavl.insert(self.binavl.root, bin_id)
        nod = self.binavl.search(self.binavl.root, bin_id)  # Assuming your search method is adapted for Bin objects
        if nod:
            nod.element = binclass

    def add_object(self, object_id, size, color):
        obj=Object(object_id,size,color)
        #print(obj.color)
        if obj.color==Color.BLUE:
            walk = self.bando.root
            found=0
            #print(self.bando.findnear(self.bando.root,[size,0]))
            path=(self.bando.findnear(self.bando.root,[size,0]))
            for i in range(1,len(path)+1):
                if path[-i].key[0]>=size:
                    break
                else:
                    continue
            walk=path[-i]
            #while walk.left is not None and (walk.left.key[0]==walk.key[0]):
                #walk=walk.left
            #if object_id==2009:
                #print(self.bando.pre_order(self.bando.root),walk.key)    
            '''walk = self.bando.root
            found=0
            while True:
                if walk.key[0]<size and walk.right is not None:
                    walk=walk.right
                    if walk.key[0]>=size:
                        found=1
                elif walk.left is not None and walk.left.key[0]>=size :  # Assuming a left method exists
                    walk = walk.left
                    found=1
                else:
                    break
            if object_id==2018:
                print(self.bando.pre_order(self.bando.root),walk.key)'''
            if walk.key[0]<size:
                raise NoBinFoundException
            else:
                (self.binavl.search(self.binavl.root,walk.key[1])).element.add_object(obj)
                self.objavl.root=self.objavl.insert(self.objavl.root, object_id)
                (self.objavl.search(self.objavl.root, object_id)).element=obj
                obj.bin0=walk.key[1]
            #print('done')
        #print(self.bando.pre_order(self.bando.root))
        elif obj.color==Color.YELLOW:
            walk = self.bando.root
            found=0
            #print(self.bando.findnear(self.bando.root,[size,0]))
            path=(self.bando.findnear(self.bando.root,[size,0]))
            for i in range(1,len(path)+1):
                if path[-i].key[0]>=size:
                    break
                else:
                    continue
            walk=path[-i]
            while walk.right is not None and (walk.right.key[0]==walk.key[0] or walk.key[0]<size):
                walk=walk.right
            '''while True:
                if walk.left is not None and walk.left.key[0]>=size and walk.left.key[0]!=walk.key[0]:  # Assuming a left method exists
                    walk = walk.left
                    found=1
                elif walk.right is not None and (walk.key[0]<size or (walk.left is not None and walk.right.key[0]==walk.left.key[0])):
                    walk=walk.right
                else:
                    break'''
            if walk.key[0]<size:
                    raise NoBinFoundException
            (self.binavl.search(self.binavl.root,walk.key[1])).element.add_object(obj)
            self.objavl.root=self.objavl.insert(self.objavl.root, object_id)
            (self.objavl.search(self.objavl.root, object_id)).element=obj
            obj.bin0=walk.key[1]
            #print(self.bando.pre_order(self.bando.root))
        elif obj.color==Color.RED:
            walk = self.bando.root
            while True:
                if walk.right is not None and walk.key[0]!=walk.right.key[0] :  # Assuming a left method exists
                    walk = walk.right
                elif walk.right is not None and walk.key[0]==walk.right.key[0] and walk.left is not None and walk.left.key[0]==walk.key[0]:
                    walk=walk.left
                else:
                    break
            if walk.key[0]>=size :
                (self.binavl.search(self.binavl.root,walk.key[1])).element.add_object(obj)
                self.objavl.root=self.objavl.insert(self.objavl.root, object_id)
                (self.objavl.search(self.objavl.root, object_id)).element=obj
                obj.bin0=walk.key[1]
            else:
                raise NoBinFoundException
        elif obj.color==Color.GREEN:
            walk = self.bando.root
            while True:
                if walk.right is not None:  # Assuming a left method exists
                    walk = walk.right
                else:
                    break
            if walk.key[0]>=size :
                (self.binavl.search(self.binavl.root,walk.key[1])).element.add_object(obj)
                self.objavl.root=self.objavl.insert(self.objavl.root, object_id)
                (self.objavl.search(self.objavl.root, object_id)).element=obj
                obj.bin0=walk.key[1]
            else:
                raise NoBinFoundException
        
        ke=copy.deepcopy(walk.key)
        self.bando.root = self.bando.delete_node(self.bando.root,walk.key)
        self.bando.root = self.bando.insert(self.bando.root,[ke[0]-size,ke[1]])
        (self.binavl.search(self.binavl.root, ke[1])).element.capacity-=size
        #print((self.binavl.search(self.binavl.root, walk.key[1])).element.capacity , walk.key[1])
    def delete_object(self, object_id):
        # Implement logic to remove an object from its bin
        #self.objavl.search(self.objavl.root,object_id)
        bininst=self.binavl.search(self.binavl.root, self.objavl.search(self.objavl.root,object_id).element.bin0).element
        bininst.remove_object(object_id)
        bininst.capacity+=self.objavl.search(self.objavl.root,object_id).element.size
        self.objavl.search(self.objavl.root,object_id).element.bin0=None
        
        pass

    def bin_info(self, bin_id):
        # returns a tuple with current capacity of the bin and the list of objects in the bin (int, list[int])
        bininst=self.binavl.search(self.binavl.root, bin_id).element
        k=bininst.objects.in_order(bininst.objects.root)
        return (bininst.capacity,bininst.objects.L)
        pass

    def object_info(self, object_id):
        return (self.objavl.search(self.objavl.root,object_id).element.bin0)        # returns the bin_id in which the object is stored
        pass
    
    

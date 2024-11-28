class Node:
    __slots__='element','key','left','right','height','objects'
    def __init__(self,key, height=1, element=None, left=None, right=None):
        self.height=height
        self.key = key 
        self.element=element
        self.left=left
        self.right=right
        self.objects=[]
        pass

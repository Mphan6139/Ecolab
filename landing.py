users = {}

class User:
    def __init__(self, name, trash, points, history):
        if self not in users:
            self.name = name
            self.points = 0
            self.trash = trash
            self.history = []
            users[self.name] = points

    def add_points(self, points, history):
        #The person throws trash in the correct bin
        self.points += 1
        users[self.name] = self.points
        self.history += self.trash
        


   
    


    

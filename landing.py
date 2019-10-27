import datetime
users = {}
recyclable_items = ['water_bottle', 'cans', 'binder_paper']
landfill = ['boba', 'popchips']
compost = ['tangerine', 'used_napkins']


def get_user(numb):
        return users[numb]
class User:
    def __init__(self, name, points=0, history=[]):
        if self not in users:
            self.name = name
            self.points = 0
            self.history = []
            users[self.name] = points

    def process_result(self, result):
        if self.trash in recyclable_items:
            return True
            self.history.append({self.name, self.points, bin, date})
        else:
            return False
    
    def change_points(self, points, history):
        #The person throws trash in the correct bin
        if self.result == True:
            self.points += 1
        else:
            self.points -= 1
        users[self.name] = self.points
       # self.history += self.trash
    def __str__(self):
        return {self.name self.points, self.history}
        

    

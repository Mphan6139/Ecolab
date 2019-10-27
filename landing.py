from datetime import date
users = {}
recyclable_items = ['Water', 'cans', 'binder paper']
landfill = ['boba', 'pop chips']
compost = ['tangerine', 'used napkins']


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
        if result in recyclable_items:
            pts = 1
            bin_name = 'Recycle Bin'
        else:
            pts = -1
        self.points += pts

        if result in landfill:
            bin_name = 'Garbage Bin'
        
        if result in compost:
            bin_name = 'Compost Bin'

        self.history.append({result, pts, bin_name, date.today()})
        return self.points > 0

    def change_points(self, points, history):
        #The person throws trash in the correct bin
            
        users[self.name] = self.points
       # self.history += self.trash
    def __str__(self):
        return {self.name, self.points, self.history}
        
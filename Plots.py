import matplotlib.pyplot as plt

class Plots:

    def __init__(self):
        self._users = {}

    def push(self, user,day,messages):
        

        if user.id not in self._users:
            self._users[user.id] = {"x":[],"y":[],"username":user.username}
        

        self._users[user.id]["x"].append(day)
        self._users[user.id]["y"].append(messages)
        
    def plot(self,axes):
        print(self._users)
        for user in self._users:
            axes.plot(self._users[user]['x'],self._users[user]['y'],label=self._users[user]['username'])
        axes.legend()





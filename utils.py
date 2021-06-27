import pickle


SECONDS_IN_DAY = 60*60*24
THREE_HOURS = 60*60*3


# floors timestamp to day 
def floor_date(date):
    return date - date % SECONDS_IN_DAY - THREE_HOURS



def save_obj(obj, name ):
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)
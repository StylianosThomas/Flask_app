''' dogs controller '''
from werkzeug.exceptions import BadRequest

dogs = [
    {'id': 1, 'name': 'Rex', 'breed': 'German Shepherd'},
    {'id': 2, 'name': 'Max', 'breed': 'Shiba Inu'},
    {'id': 3, 'name': 'Marley', 'breed': 'Poodle'} 
]

def index(req):
    return [d for d in dogs], 200

def show(req, uid):
    return findById(uid), 200

def create(req):
    new_dog = req.get_json()
    new_dog['id'] = sorted([d['id'] for d in dogs])[-1] +1
    dogs.append(new_dog)
    return new_dog, 201

def update(req, uid):
    dog = findById(uid)
    data = req.get_json()
    print(data)
    for key, val in data.items():
        dog[key] = val
    return dog, 200

def destroy(req, uid):
    dog = findById(uid)
    dogs.remove(dog)
    return dog, 204

def findById(uid):
    try:
        return next(dog for dog in dogs if dog['id'] == uid)
    except:
        raise BadRequest(f"Dog with id {uid}, does not exist")
''' owners controller '''
from werkzeug.exceptions import BadRequest

owners = [
    {'id': 1, 'name': 'Richard Moser', 'owns': 'Rex'},
    {'id': 2, 'name': 'Bob', 'owns': 'Marley, Max'} 
]

def index(req):
    return [o for o in owners], 200

def show(req, uid):
    return findById(uid), 200

def create(req):
    new_owner = req.get_json()
    new_owner['id'] = sorted([o['id'] for o in owners])[-1] +1
    owners.append(new_owner)
    return new_owner, 201

def update(req, uid):
    owner = findById(uid)
    data = req.get_json()
    print(data)
    for key, val in data.items():
        owner[key] = val
    return owner, 200

def destroy(req, uid):
    owner = findById(uid)
    owners.remove(owner)
    return owner, 204

def findById(uid):
    try:
        return next(owner for owner in owners if owner['id'] == uid)
    except:
        raise BadRequest(f"Owner with id {uid}, does not exist")
import json,os
data={
    "userId": 1,
    "id": 1,
    "title": "delectus aut autem",
    "completed": False
}
import pathlib
print(pathlib.Path().absolute())
path_to_file=pathlib.Path().absolute()
path_to_file=os.path.join(path_to_file,'data.json')
data={}

with open(path_to_file, "w") as write_file:
    json.dump(data, write_file)


with open(path_to_file, "r") as read_file:
    data = json.load(read_file)
    
data['name']='vikas'

with open(path_to_file, "w") as write_file:
    json.dump(data, write_file)


with open(path_to_file, "r") as read_file:
    data = json.load(read_file)
print(data)
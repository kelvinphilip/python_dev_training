thisdict = {
    "brand": "Ford",
    "type" : "car",
    "wheels" : 4,
    "sold" : False,
    "owners" : ["Kelvin", "Kashyap"],
    "metadata" : {
        "color" : "red", 
        "transmission" : "auto", 
        "engine_cc" : 500
        }
}

# for x in thisdict.keys():
    # print(x)

# for y in thisdict.values():
    # print(f'type = {type(y)} and value = {y}')

for key,value in thisdict.items():
    if isinstance(value, dict):
        for k,v in value.items():
            print(f'parent_key = {key} and child_key = {k}, child_value = {v}')
    elif isinstance(value, list):
        for v in value:
             print(f'key = {key} , child_value = {v}')
    else:
        print(f'key = {key} , value = {value}')




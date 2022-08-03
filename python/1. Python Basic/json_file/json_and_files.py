import json

# Variable to generate the address file
add = {
    'alpha': {
        'name': "alpha",
        "address": "276000, linyi university, lanshang,linyi city",
        "phone": 1835491926
    }, 'andrea': {
        'name': "andrea",
        "address": "276000, linyi university, lanshang,linyi city",
        "phone": 1526519052
    }
}

print("-----Creating and writing file with json content-----")
# Formation the dictionary ADD to JSON
formatting_to_json = json.dumps(add)
# Creating and writting the json data in a file
with open("/Volumes/Data/Code/python/learning/firstproject/json_file/address.txt", "w") as f:
    f.write(formatting_to_json)

# Reading the file content
print("-----Reading the file content-----")
file_content = open("/Volumes/Data/Code/python/learning/firstproject/json_file/address.txt", "r")
string_content = file_content.read()
print(string_content)

# Reading the file content as JSON
print("-----Reading the file content as JSON")
json_content = json.loads(string_content)
print(json_content)

# Reading values from the file content JSON
print("----Reading values from the file content JSON")
value = json_content['alpha']
sub_value = json_content['alpha']["address"]
print(value)
print(sub_value)

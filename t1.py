import csv
# with open("./files/people.csv","w",newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["name","Age"])
#     writer.writerow(["Omkar","29"])
#     writer.writerow(["Vishal","6"])

# with open("./files/people.csv","r",newline="") as file:
#     temp = csv.DictReader(file.readlines())
#     print(list(x["name"] for x in list(temp)))

import json

dictionary = {
    "name": "Omkar",
    "rollno": 29,
}

json_object = json.dumps(dictionary, indent=4)


with open("./files/peoples.json", "w") as outfile:
    outfile.write(json_object)

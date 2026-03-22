# get rid of duplicates
student_data = {
    "id1" : {
        "name": "Mithran",
        "age":15,
        "subject":['english','geography','civics']
    },
    "id2":{
        "name": "Neerav",
        "age":14,
        "subject":['hindi','history','civics']
    },
    "id3":{
        "name": "Mithran",
        "age":15,
        "subject":['english','geography','civics']
    },
    "id4":{
        "name": "Ravin",
        "age":15,
        "subject":['english','science','sst']
    }
}
print("the original dictionary")
print(student_data)
unique_dict = {}
for key,value in student_data.items():
    if value not in unique_dict.values():
        unique_dict[key] = value
print("after removing the dupicate")
print(unique_dict)
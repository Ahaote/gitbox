import json

# 序列化
data = {
    "name" : "张三",
    "age" : 30,
    "courses" : ["Python", "Data"],
    "is_student" : False
}

json_str = json.dumps(data, ensure_ascii=False, indent=4)
print(json_str)


# 反序列化
json_data = '{"name": "李四", "score": 95.5}'
python_dict = json.loads(json_data)
print(python_dict["name"])
print(type(python_dict))

# 写入JSON文件
with open(".\data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

with open("data.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)

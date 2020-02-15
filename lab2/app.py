from flask import Flask, escape, request
from flask import make_response

app = Flask(__name__)

database = {
    "students": [],
    "classes": []
}


@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'


@app.route('/students', methods=['POST'])
def create_student():
    # print('hello')

    student_name = request.json.get('name')

    student_id = 1234456
    temp_student = {
        "id": student_id,
        "name": student_name
    }
    database["students"].append(temp_student)
    return {"id": student_id, "name": student_name}, 201
    
@app.route('/students', methods=['GET'])

# def get_student():
    
#     student_id = request.args.get('id')

#     database["students"].append(temp_student)
#     return {"id": student_id, "name": student_name}, 201


@app.route('/classes', methods=['POST'])
def create_class():
    # print('hello')
    class_name = request.json.get('name')
    print(class_name)
    class_id = 1122334
    student = []

    temp_class = {
        "id": class_id,
        "name": class_name,
        "students": student
    }
    database["classes"].append(temp_class)
    return {"id": class_id, "name": class_name, "students": "Rui Yang"}, 201

from flask import Flask, escape, request
from flask import make_response

app = Flask(__name__)

database = {
    "students": {

    },
    "classes": {

    }
}


# @app.route('/<id>')
# def hello(id):
#     name = request.args.get("name", "World")
#     return f'Hello, id,{escape(name)}!'


@app.route('/students', methods=['POST'])
def create_student():

    student_name = request.json.get('name')

    student_id = 1234456
    temp_student = {
        student_id: student_name,
    }
    database['students'].update(temp_student)
    # print(database)

    return {"id": student_id, "name": student_name}, 201


@app.route('/students/<id>', methods=['GET'])
def get_student_info(id):

    student_id = int(id)

    if student_id in database['students']:
        return {"id": student_id, "name": database['students'].get(student_id)}, 201
    else:
        return {"Error Message": "No such student id"}, 204


@app.route('/classes', methods=['POST'])
def create_class():

    class_name = request.json.get('name')

    class_id = 1122334
    temp_class = {
        'id': class_id,
        "name": class_name,
        "students": []
    }

    database["classes"].update(temp_class)
    return {"id": class_id, "name": class_name, "students": database['classes']['students']}, 201


@app.route('/classes/<id>', methods=['PATCH'])
def register_course(id):

    student_id = int(request.json.get('student_id'))
    course_id = id

    student_name = database["students"].get(student_id)

    temp_student = {
        "id": student_id,
        "name": student_name
    }

    database["classes"].get("students").append(temp_student)

    return {"id": course_id, "name": database['classes']['name'], "students": database['classes']['students']}, 201

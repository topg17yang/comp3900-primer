from flask import Flask, jsonify, request
from flask_cors import CORS

import db

app = Flask(__name__)
CORS(app)

# Instructions:
# - Use the functions in backend/db.py in your implementation.
# - You are free to use additional data structures in your solution
# - You must define and tell your tutor one edge case you have devised and how you have addressed this

@app.route("/students")
def get_students():
    """
    Route to fetch all students from the database
    return: Array of student objects
    """
    
    # TODO: replace with your implementation. This is a mock response
    return jsonify(db.get_all_students()), 200


@app.route("/students", methods=["POST"])
def create_student():
    """
    Route to create a new student
    param name: The name of the student (from request body)
    param course: The course the student is enrolled in (from request body)
    param mark: The mark the student received (from request body)
    return: The created student if successful
    """

    # Getting the request body - replace with your implementation
    student_data = request.json
    name = student_data.get("name")
    course = student_data.get("course")
    mark = student_data.get("mark")


    #edge case 1:
    # have to check if the name / course is None or not
    if name is None or course is None:
        return jsonify({"error": "name and course is needed"}), 400


    return jsonify(db.insert_student(name, course, mark)), 200
    # pass





@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    """
    Route to update student details by id
    param name: The name of the student (from request body)
    param course: The course the student is enrolled in (from request body)
    param mark: The mark the student received (from request body)
    return: The updated student if successful
    """
    student_data = request.json
    name = student_data.get("name")
    course = student_data.get("course")
    mark = student_data.get("mark")

    updated_stud = db.update_student(student_id, name, course, mark)

    if updated_stud is None:
        return jsonify({"error": "id does not exist"}), 404

    return jsonify(updated_stud), 200
    # pass  # replace with your implementation


@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    """
    Route to delete student by id
    return: The deleted student
    """

    remove_stud = db.delete_student(student_id)

    if remove_stud is None:
        return jsonify({"error": "student not found"}), 404

    return jsonify(remove_stud), 200
    # pass  # replace with your implementation



@app.route("/stats")
def get_stats():
    """
    Route to show the stats of all student marks 
    return: An object with the stats (count, average, min, max)
    """

    all_stud = db.get_all_students()

    
    marks = [s["mark"] for s in all_stud if s["mark"] is not None]

    # edge case 2:
    # if all students mark is None, it will cause a zero division error, as 
    # when getting the average, 0 / 0. 

    if len(marks) == 0:
        stats = {
            "count": len(marks),
            "average": None,
            "min": None,
            "max": None
        } 
    else:
        stats = {
            "count": len(marks),
            "average": sum(marks) / len(marks),
            "min": min(marks),
            "max": max(marks)
        } 


    return jsonify(stats), 200
    # pass  # replace with your implementation






@app.route("/")
def health():
    """Health check."""
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

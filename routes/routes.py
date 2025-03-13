from flask import Blueprint, request, jsonify
from models import TaskModel
routes_blueprint=Blueprint("routes",__name__)
@routes_blueprint.route("/addTask", methods=["POST"])
def add_task():
    data = request.get_json()
    if data is None:
        return {"message": "Bad request"}, 400
    if "task" not in data:
        return jsonify({
            "message":"bad request!"
        }),400
    task_to_save={
        "task":data["task"]
    }
    result=TaskModel.add_task(task_to_save)
    return jsonify(result)

@routes_blueprint.route("/allTasks", methods=["GET"])  
def get_tasks():
    result = TaskModel.getAllTasks() 
    return jsonify(result)
@routes_blueprint.route("/task/<task_id>",methods=["GET"])
def get_task(task_id):
    if not task_id:
        return{
            "message":"bad request, task id is required!"
        },400
    task=TaskModel.get_task_by_id(task_id)
    return jsonify(task)
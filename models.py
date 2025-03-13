from db import task_collection
from bson import json_util, ObjectId

class TaskModel:
    @staticmethod
    def add_task(task_data):
        try:
            original_data = task_data.copy()
            result = task_collection.insert_one(task_data)
            return {
                "task_data": original_data,
                "id": str(result.inserted_id)
            }, 200
        except Exception as e:
            print(e)
            return {"error": "Internal server error"}, 500
    @staticmethod
    def getAllTasks():
        try:
            tasks=list(task_collection.find({}))
            for task in tasks:
                task['_id']=str(task['_id'])
            return {
                "tasks":tasks
            },200
        except Exception as e:
            print(e)
            return {
                "message":"error fetching tasks!"
            },500
    @staticmethod
    def get_task_by_id(task_id):
        try:
            object_id=ObjectId(task_id)
            task=task_collection.find_one({"_id":object_id})
            if not task:
                return {
                    "message":"Task not found!"
                },404
            task["_id"]=str(task['_id'])
            return{
                "task":task
            },200
        except Exception as e:
            print(e)
            return{
                "message":"Internal Server error!"
            },500
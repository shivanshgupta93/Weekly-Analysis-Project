from flask import jsonify
import json

def deserializer(request_obj):
    return request_obj.json()
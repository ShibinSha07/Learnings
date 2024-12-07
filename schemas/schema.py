def individual_serializer(todo)->dict:
    return{
        "id":str(todo["_id"]),
        "name":str(todo["name"]),
        "description":str(todo["description"]),
        "complete":str(todo["complete"])
    }
    
def list_serializers(todos)->list:
    return [individual_serializer(todo) for todo in todos]
from enum import Enum

from fastapi import FastAPI
#wpetty to run server (from fast_api root): uvicorn main:paramsapp --reload


class ModelName(str, Enum):
    alexnet = "alexnet"
    lenet = "lenet"
    resnet = "resnet"

paramsapp = FastAPI()


#wpetty sample .get()
@paramsapp.get("/home")
def root():
    return {"message": "FastAPI Project"}


#wpetty sample path parameters function
@paramsapp.get("/items/{item_id}")
#wpetty item_id: int - validation effort through type annotation, returns 422 if not an int
def pathparams(item_id: int):
    return {"item_id": item_id}


#wpetty order of operations matters
#wpetty if you duplicate path names, it will run the top function in codebase
@paramsapp.get("/users/me")
def read_user_me():
    return {"user_id": "the current user"}

#wpetty this func will have to be after the one just above, otherwise, you will
#wpetty never be able to access user 'me' because you are then redefining 'me' as a user_id
@paramsapp.get("/users/{user_id}")
def read_user(user_id: str):
    return {"user_id": user_id}


@paramsapp.get("/models/{model_name}")
#wpetty note Class for type annotation
def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": f"I don't know what {model_name} is!"}
    elif model_name.value == 'lenet':
        return {"model_name": model_name, "message": f"I think this worked, {model_name}"}
    else:
        return {"model_name": model_name, "message": f"You hit the else by entering the third value, {model_name}"}
    

#wpetty :path here allows for a string value with full filepath to be appended to /files/
@paramsapp.get("/files/{file_path:path}")
#wpetty test with url: localhost:8000/files/appfiles/files/testfile.txt to see good example
def read_file(file_path: str):
    return {"file_path": file_path}
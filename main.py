from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello FastAPI"}
https://github.com/matsuteru82/my-fastapi-project/tree/main

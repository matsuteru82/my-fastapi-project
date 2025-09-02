from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello FastAPI"}

#
# 新しいエンドポイント
#
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    """
    item_id: パスパラメータ（必須, int型）
    q: クエリパラメータ（任意, str型）
    """
    return {"item_id": item_id, "q": q}


# https://github.com/matsuteru82/my-fastapi-project/tree/main


# https://kika-barcode-app.onrender.com/items/123

# https://kika-barcode-app.onrender.com/items/123?q=test

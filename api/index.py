from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "status": "success",
        "message": "FastAPI is working on Vercel!"
    }

@app.get("/api")
def api_test():
    return {
        "status": "success",
        "message": "The /api route is working!"
    }

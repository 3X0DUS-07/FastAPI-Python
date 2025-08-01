from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/projects")
def get_projects():
    return {
        "projects": [
            {"id": 1, "name": "Proyecto A", "status": "active"},
            {"id": 2, "name": "Proyecto B", "status": "inactive"},
        ]
    }

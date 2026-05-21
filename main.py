from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "project": "Cloud-Native CI/CD Pipelines with GitOps",
        "team": [
            {
                "name": "Mykyta Yevchuk",
                "student_id": "73369"
            },
            {
                "name": "Sialitski Bagdan",
                "student_id": "71669"
            }
        ],
        "status": "GitOps Pipeline is fully automated!"
    }
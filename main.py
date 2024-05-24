from fastapi import FastAPI

from search import add_data, search_data

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    add_data()


@app.get("/")
async def root():
    return {"message": "running"}


@app.get("/doctor/{doctor_name}")
async def search_doctor(doctor_name: str):
    return search_data(doctor_name)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

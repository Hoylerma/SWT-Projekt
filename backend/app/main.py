from fastapi import FastAPI

app = FastAPI(title="WG Cook")


@app.get("/api/v1/health")
def health():
    return {"status": "ok"}

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="English Project API",
    description="API for giving questions and answers",
    version="0.0.1",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # Vite development port
        "http://localhost:3000",  # Docker frontend port
        "http://frontend:3000"    # Docker internal network
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

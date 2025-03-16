from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import auth
from .utils.auth import get_current_active_user

app = FastAPI(
    title="English Project API",
    description="API for giving questions and answers",
    version="0.0.1",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins - for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

# Inclure les routeurs
app.include_router(auth.router)

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/protected-route")
async def protected_route(user=Depends(get_current_active_user)):
    return {"message": f"Bonjour {user.username}, vous avez accès à cette route protégée"}

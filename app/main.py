from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware

from . import models 
from .database import engine
from .routers import post, user, auth
from .config import settings

# this command tells sqlalchemy to run the create statements that will generate all the tables whe it all started up but we don't need it since we have alembic now
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


@app.get("/")
def root():
    return {"message": "Hello World!"}




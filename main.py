from typing import Optional  
from fastapi import FastAPI

#routers
from routes.user import users

app = FastAPI(
    title='Manage System',
    description='System for user managment',
    version="0.0.1",
    openapi_tags=[{
        'name': 'users',
        'description': 'user manage endpoints'
    }]
)

#Third part routers
app.include_router(users)

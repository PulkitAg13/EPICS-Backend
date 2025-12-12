from fastapi import FastAPI
from routers import auth_routes, disease_routes, market_routes, stock_routes, residue_routes
from database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_routes.router)
app.include_router(disease_routes.router)
app.include_router(market_routes.router)
app.include_router(stock_routes.router)
app.include_router(residue_routes.router)

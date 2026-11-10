import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from backend.api.overview import router as overview_router
from backend.api.players import router as players_router
from backend.api.pressure import router as pressure_router
from backend.api.compare import router as compare_router
from backend.api.auction import router as auction_router
from backend.api.methodology import router as methodology_router

app = FastAPI(
    title="ROYAL EDGE API",
    description="Rajasthan Royals | IPL 2027 Auction Intelligence Platform Backend API",
    version="1.0.0"
)

# CORS Middleware to allow requests from Vite dev server and frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(overview_router)
app.include_router(players_router)
app.include_router(pressure_router)
app.include_router(compare_router)
app.include_router(auction_router)
app.include_router(methodology_router)

# Mount outputs/figures if exists for static image delivery
outputs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "outputs"))
if os.path.exists(outputs_dir):
    app.mount("/static/outputs", StaticFiles(directory=outputs_dir), name="outputs")

# Mount stitch_screens if exists
stitch_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "stitch_screens"))
if os.path.exists(stitch_dir):
    app.mount("/static/stitch", StaticFiles(directory=stitch_dir), name="stitch")

@app.get("/")
def root():
    return {
        "platform": "ROYAL EDGE",
        "team": "Rajasthan Royals",
        "season": "IPL 2027 Auction Intelligence",
        "status": "online",
        "docs_url": "/docs"
    }

@app.get("/health")
def health():
    return {"status": "healthy", "service": "royal-edge-fastapi"}


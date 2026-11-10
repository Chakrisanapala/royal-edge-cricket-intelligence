import os
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.exceptions import HTTPException as StarletteHTTPException

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

# CORS Middleware allowing production Netlify domain, preview deploys, and local dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://royal-edge-cricket-intelligence.netlify.app",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "*"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Exception handlers ensuring pure JSON responses (never HTML fallback)
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": True, "status_code": exc.status_code, "detail": exc.detail}
    )

@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"error": True, "status_code": 500, "detail": str(exc)}
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
        "environment": "production",
        "docs_url": "/docs"
    }

# Dual health endpoint support: /api/health and /health
@app.get("/api/health")
@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "royal-edge-fastapi",
        "matches_indexed": 867,
        "deliveries_indexed": 200999
    }

if __name__ == "__main__":
    import uvicorn
    # Compatible with Render's dynamic $PORT environment variable
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("backend.main:app", host="0.0.0.0", port=port, reload=False)

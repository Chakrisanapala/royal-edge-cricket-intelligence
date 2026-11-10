# RENDER DEPLOYMENT GUIDE — FASTAPI BACKEND
## Project: ROYAL EDGE — Rajasthan Royals IPL 2027 Auction Intelligence
**Target Platform:** Render Web Service (Python 3.11/3.12/3.14)  
**Repository:** `https://github.com/Chakrisanapala/royal-edge-cricket-intelligence.git`  
**Public Netlify Domain Allowed:** `https://royal-edge-cricket-intelligence.netlify.app`

---

## 1. Quick Reference: Verified Render Configuration

| Parameter | Exact Value | Notes |
| :--- | :--- | :--- |
| **Backend Entry Point** | `backend/main.py` | Contains `app = FastAPI(...)` and dual health routes |
| **Exact Uvicorn Path** | `backend.main:app` | Standard module:variable syntax |
| **Dependency File** | `requirements.txt` *(or `backend/requirements.txt`)* | Contains `fastapi`, `uvicorn[standard]`, `pydantic`, `pandas`, `numpy`, `scipy`, `pyarrow` |
| **Root Directory** | *(leave blank)* | Points to repository root |
| **Build Command** | `pip install -r requirements.txt` | Installs verified dependencies in Linux container |
| **Start Command** | `uvicorn backend.main:app --host 0.0.0.0 --port $PORT` | Binds dynamically to Render's assigned port |
| **Environment Variable** | `PYTHON_VERSION = 3.11.9` | Recommended stable Python runtime |

---

## 2. Option A: 1-Click Blueprint Deployment (Recommended)

A pre-configured `render.yaml` file is placed in your repository root:

1. Log into your **[Render Dashboard](https://dashboard.render.com/)**.
2. Click **New +** in the top navigation and select **Blueprint**.
3. Connect your GitHub account and select: `Chakrisanapala/royal-edge-cricket-intelligence`.
4. Render automatically reads `render.yaml` and sets:
   - **Service Name:** `royal-edge-backend`
   - **Runtime:** `Python`
   - **Plan:** `Free`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`
5. Click **Apply**.
6. Render builds the container and launches the API in ~2 minutes.

---

## 3. Option B: Manual Web Service Setup

If you prefer manually setting up the service in Render:

1. In **Render Dashboard**, click **New + > Web Service**.
2. Select **Build and deploy from a Git repository**.
3. Choose `Chakrisanapala/royal-edge-cricket-intelligence`.
4. Enter the following exact settings:
   - **Name:** `royal-edge-backend` (or your preferred unique service name)
   - **Region:** `Oregon (US West)` or `Frankfurt (EU Central)`
   - **Branch:** `main`
   - **Root Directory:** *(leave blank)*
   - **Runtime:** `Python`
   - **Build Command:**
     ```bash
     pip install -r requirements.txt
     ```
   - **Start Command:**
     ```bash
     uvicorn backend.main:app --host 0.0.0.0 --port $PORT
     ```
   - **Instance Type:** `Free`
5. Under **Advanced**, click **Add Environment Variable**:
   - **Key:** `PYTHON_VERSION`
   - **Value:** `3.11.9`
6. Click **Create Web Service**.

---

## 4. Post-Deployment Verification on Render

Once Render reports that the deployment is live:
1. **Health Check:**
   ```bash
   curl -I https://<your-render-service-name>.onrender.com/api/health
   ```
   *Expected Response:*
   ```json
   {
     "status": "healthy",
     "service": "royal-edge-fastapi",
     "matches_indexed": 867,
     "deliveries_indexed": 200999
   }
   ```
2. **Batters Ranking:**
   `https://<your-render-service-name>.onrender.com/api/players/batters`
3. **Bowlers Ranking:**
   `https://<your-render-service-name>.onrender.com/api/players/bowlers?actionable_only=true`
4. **Interactive Swagger Docs:**
   `https://<your-render-service-name>.onrender.com/docs`

---

## 5. Next Step: Connect to Netlify

Once your Render backend URL is live, follow [**`NETLIFY_BACKEND_CONNECTION_GUIDE.md`**](file:///d:/Desktop/RR%20-%20Hackathon/NETLIFY_BACKEND_CONNECTION_GUIDE.md) to set `VITE_API_URL` in Netlify and trigger a redeploy.

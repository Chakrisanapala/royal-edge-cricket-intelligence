# NETLIFY TO RENDER BACKEND CONNECTION GUIDE
## Project: ROYAL EDGE — Rajasthan Royals IPL 2027 Auction Intelligence Platform
**Netlify URL:** `https://royal-edge-cricket-intelligence.netlify.app`  
**GitHub Repository:** `Chakrisanapala/royal-edge-cricket-intelligence`

---

## 1. Problem Resolution Overview

### Issue Encountered on Netlify:
```text
Unexpected token '<', "<!doctype "... is not valid JSON
```

### Why this happens:
Netlify hosts the compiled static React SPA frontend. When the frontend attempts to call `/api/overview`, Netlify cannot run the Python FastAPI backend. Due to SPA routing, Netlify serves `index.html` (which begins with `<!doctype html>`) in place of missing API routes. When the JavaScript code calls `.json()`, parsing an HTML page fails with the syntax error above.

### Solution:
Connect your public Netlify frontend to your newly deployed public FastAPI backend on Render using the environment variable `VITE_API_URL`.

---

## 2. Step-by-Step Connection Instructions

### Step 1: Deploy Backend on Render
Deploy your FastAPI backend following [**`RENDER_DEPLOYMENT_GUIDE.md`**](file:///d:/Desktop/RR%20-%20Hackathon/RENDER_DEPLOYMENT_GUIDE.md).  
Your live Render backend URL will look like:
```text
https://royal-edge-backend.onrender.com
```

### Step 2: Verify the Live Backend
Test your live backend in any browser or terminal:
```bash
curl -I https://royal-edge-backend.onrender.com/api/health
```
Expected response:
```json
{
  "status": "healthy",
  "service": "royal-edge-fastapi",
  "matches_indexed": 867,
  "deliveries_indexed": 200999
}
```

### Step 3: Configure Netlify Environment Variable
1. Log into your **[Netlify Dashboard](https://app.netlify.com/)**.
2. Select your site: **`royal-edge-cricket-intelligence`**.
3. Go to **Site configuration** > **Environment variables**.
4. Click **Add a variable** > **Add a single variable**:
   - **Key:** `VITE_API_URL`
   - **Value:** `https://royal-edge-backend.onrender.com/api`
   - **Scopes:** All scopes (Builds, Functions, Post-processing, etc.)
5. Click **Create variable**.

*(Note: The frontend code in `frontend/src/services/api.ts` automatically formats the URL and appends `/api` if omitted).*

### Step 4: Trigger a Clean Netlify Redeploy
Because Vite bakes `import.meta.env.VITE_API_URL` into client assets at build time, Netlify must rebuild the project with the new variable:
1. In your Netlify site dashboard, navigate to the **Deploys** tab.
2. Click the **Trigger deploy** dropdown button.
3. Select **Clear cache and deploy site**.
4. Wait ~1 minute for the build to finish.

### Step 5: Verify the Live Frontend
Open [**`https://royal-edge-cricket-intelligence.netlify.app`**](https://royal-edge-cricket-intelligence.netlify.app):
- The dashboard should load immediately without the `<!doctype` syntax error.
- The 4 KPI cards will show **867 Matches**, **200,999 Deliveries**, and **45,951 High Pressure Balls**.
- All 8 navigation screens (`/pressure`, `/batting`, `/bowling`, `/compare`, `/auction`, `/profiles`, `/methodology`) will function with live data.


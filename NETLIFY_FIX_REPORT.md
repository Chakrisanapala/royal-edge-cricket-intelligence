# NETLIFY DEPLOYMENT DIAGNOSIS & REPAIR REPORT
## Project: ROYAL EDGE — Rajasthan Royals IPL 2027 Auction Intelligence
**Target URL:** `https://royal-edge-cricket-intelligence.netlify.app`  
**Repository:** `https://github.com/Chakrisanapala/royal-edge-cricket-intelligence.git`  
**Audit Date:** November 10, 2026  
**Status:** **DIAGNOSED & CONFIGURATION PREPARED (PENDING USER COMMIT APPROVAL)**

---

## 1. Actual Deployment Diagnosis (Evidence-Based)

A live HTTP query against `https://royal-edge-cricket-intelligence.netlify.app` was conducted using `Invoke-WebRequest`:
```text
HTTP Status: 404 Not Found
Server: Netlify
Body: "Not Found - Request ID: 01M739FGMETTZTYBA3K7J07WDG"
      "Build and deploy your own site for free: https://netlify.new/..."
```

### Root Causes Identified:

1. **Subdirectory Project Structure without `netlify.toml`:**
   - In your GitHub repository, the React/Vite web application resides in the `frontend/` subdirectory, whereas Python backend files (`backend/`, `data/`, `final_submission/`) reside at the repository root.
   - When a repository is connected to Netlify without a root `netlify.toml`, Netlify defaults to searching for `package.json` at the root directory (`/`).
   - Because no root `package.json` exists, Netlify could not detect the Node/Vite build system or automatically determine the publish directory, resulting in no site build being published.

2. **Absence of Single Page Application (SPA) Redirects:**
   - React Router uses HTML5 `pushState` for client-side navigation (`/pressure`, `/batting`, `/bowling`, `/compare`, `/auction`, `/profiles`, `/methodology`).
   - Without an explicit redirect rule (`/* /index.html 200`), direct visits or page refreshes on any subroute return a Netlify 404 error.

3. **Backend Architecture Separation:**
   - Netlify is a static edge CDN platform. It cannot execute long-running Python FastAPI services or ASGI servers like Uvicorn.
   - The frontend's API client was previously initialized to `const API_BASE = '/api';`. On Netlify, this would route to a non-existent static `/api` directory unless configured with an external backend URL (`VITE_API_URL`) or an HTTP proxy redirect.

---

## 2. Technical Fixes Implemented Locally

### A. Created Root `netlify.toml`
Located at: `d:\Desktop\RR - Hackathon\netlify.toml`
```toml
# Netlify Build and Routing Configuration for ROYAL EDGE

[build]
  base = "frontend"
  publish = "dist"
  command = "npm run build"

[build.environment]
  NODE_VERSION = "20"

# SPA Fallback: Route all client URLs to index.html
[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200

# Security and cache headers
[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "DENY"
    X-Content-Type-Options = "nosniff"
    Referrer-Policy = "strict-origin-when-cross-origin"
```

### B. Created SPA Redirects in Public Directory
Located at: `d:\Desktop\RR - Hackathon\frontend\public\_redirects`
```text
# Single Page App routing for React Router
/*    /index.html   200
```
*Note:* Vite automatically copies files in `public/` directly into `frontend/dist/` during the production build.

### C. Dynamic API Base URL Configuration in Frontend
Located at: `d:\Desktop\RR - Hackathon\frontend\src\services\api.ts`
```typescript
// Support VITE_API_URL for Render backend or fallback to /api (Netlify proxy / local Vite)
const rawBase = (import.meta.env.VITE_API_URL as string | undefined) || '/api';
const API_BASE = rawBase.replace(/\/$/, '');
```
- In local development, it defaults to `/api` (proxied by Vite to `http://127.0.0.1:8000`).
- In Netlify production, setting the environment variable `VITE_API_URL` (e.g. `https://royal-edge-backend.onrender.com/api`) directs all analytics and auction requests to the deployed Render FastAPI backend.

### D. Verified Local Production Build
```text
> frontend@0.0.0 build
> tsc -b && vite build

vite v8.3.7 building client environment for production...
✓ 2468 modules transformed.
dist/index.html                   0.45 kB │ gzip:   0.29 kB
dist/assets/index-XMKvVtXO.css   35.54 kB │ gzip:   6.77 kB
dist/assets/index-D3vI_1RK.js   777.30 kB │ gzip: 220.24 kB
dist/_redirects                   0.06 kB
✓ built in 2.49s (0 errors)
```

---

## 3. Required Netlify Web Dashboard Steps

Once you approve pushing the commit to GitHub:
1. Log into **[Netlify](https://app.netlify.com/)**.
2. If the site `royal-edge-cricket-intelligence` already exists:
   - Navigate to **Site configuration > Build & deploy > Continuous deployment**.
   - Confirm **Base directory** is set to `frontend` (or leave default if reading `netlify.toml`).
   - Confirm **Publish directory** is set to `dist` (or `frontend/dist`).
   - Confirm **Build command** is `npm run build`.
3. If creating a new site:
   - Click **Add new site > Import an existing project > GitHub**.
   - Select `Chakrisanapala/royal-edge-cricket-intelligence`.
   - Netlify will automatically detect `netlify.toml` and populate:
     - Base directory: `frontend`
     - Build command: `npm run build`
     - Publish directory: `frontend/dist`
4. Set the Site Name to `royal-edge-cricket-intelligence` under **Site configuration > General > Site details > Change site name**.
5. Once your Render backend is deployed, go to **Environment variables** in Netlify and add:
   - Key: `VITE_API_URL`
   - Value: `https://<your-render-service-name>.onrender.com/api`
   - Click **Deploy site** (or trigger a new deploy).


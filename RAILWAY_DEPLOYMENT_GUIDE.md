# 🚂 Railway Backend Deployment Guide

## Quick Status Check
- ✅ Backend Code: Ready (`backend/main.py`)
- ✅ Dependencies: Listed (`backend/requirements.txt`)
- ✅ Configuration: Complete (`backend/railway.toml`, `backend/Procfile`)
- ✅ CORS: Fixed for Vercel frontend
- ❌ **Deployment: NOT DEPLOYED** (Action Required)

---

## 📋 Step-by-Step Railway Deployment

### **Step 1: Access Railway Dashboard**

1. Go to: **https://railway.app/dashboard**
2. Sign in with your GitHub account

---

### **Step 2: Find or Create Your Project**

#### **Option A: If Project Exists** (proactive-manifestation-production)
1. Click on **"proactive-manifestation-production"** project
2. Go to **Settings** tab
3. Check the following:
   - **Source Repo:** Should be `sivaramanrajagopal/OpenAIAstroPrediction`
   - **Branch:** Should be `main`
   - **Root Directory:** Must be set to **`backend`** ⚠️ CRITICAL!

#### **Option B: If Project Doesn't Exist** (Create New)
1. Click **"New Project"**
2. Select **"Deploy from GitHub repo"**
3. Choose: `sivaramanrajagopal/OpenAIAstroPrediction`
4. Click **"Deploy Now"**

---

### **Step 3: Configure Root Directory** ⚠️ MOST IMPORTANT

Railway needs to know your backend is in the `backend/` folder:

1. In your Railway project, click **"Settings"**
2. Scroll to **"Service Settings"**
3. Find **"Root Directory"** field
4. Enter: **`backend`**
5. Click **"Save"**

**Why this matters:** Without this, Railway will try to deploy from the root directory and won't find your `main.py` file!

---

### **Step 4: Set Environment Variables**

1. In Railway, go to **"Variables"** tab
2. Click **"+ New Variable"**
3. Add the following:

```bash
OPENAI_API_KEY=sk-proj-your-actual-openai-api-key-here
PORT=8000
PYTHONPATH=/app
ENVIRONMENT=production
```

**⚠️ CRITICAL:** Replace `sk-proj-your-actual-openai-api-key-here` with your real OpenAI API key!

**Where to get OpenAI API Key:**
- Go to: https://platform.openai.com/api-keys
- Click "Create new secret key"
- Copy the key (starts with `sk-proj-...`)
- Paste it in Railway

---

### **Step 5: Verify Deployment Configuration**

Railway will automatically detect your configuration from these files:

#### **`backend/railway.toml`** (Already configured ✅)
```toml
[build]
builder = "nixpacks"
buildCommand = "pip install -r requirements.txt"

[deploy]
startCommand = "uvicorn main:app --host 0.0.0.0 --port $PORT --log-level info"
healthcheckPath = "/health"
healthcheckTimeout = 300
restartPolicyType = "always"

[env]
PYTHONPATH = "/app"
PORT = "8000"
```

#### **`backend/Procfile`** (Already configured ✅)
```
web: uvicorn main:app --host 0.0.0.0 --port $PORT --log-level info
```

#### **`backend/requirements.txt`** (Already configured ✅)
All dependencies are listed and will be installed automatically.

---

### **Step 6: Deploy!**

1. **Trigger Deployment:**
   - Click **"Deploy"** button in Railway dashboard
   - OR push a new commit to GitHub (auto-deploys)

2. **Monitor Deployment:**
   - Watch the **"Deployments"** tab
   - Check build logs for errors
   - Should see: ✅ Build successful → ✅ Deploy successful

3. **Expected Build Time:** 3-5 minutes

---

### **Step 7: Verify Deployment**

Once deployed, test your backend:

#### **Test Health Endpoint:**
```bash
curl https://proactive-manifestation-production.up.railway.app/health
```

#### **Expected Response:**
```json
{
  "status": "healthy",
  "timestamp": "2025-12-23T...",
  "version": "2.0.0-WORKING-REPO",
  "message": "Vedic Astrology API with Working Repository Calculations!",
  "swiss_ephemeris": true,
  "astrology_modules": true,
  "astrology_engine": "AstrologyResearchDatabase-Compatible"
}
```

#### **If You Get 404:**
- Root directory is NOT set to `backend/`
- Go back to Step 3 and fix it!

---

## 🔧 Common Issues & Fixes

### **Issue 1: "Application not found" (404)**
**Cause:** Root directory not set to `backend/`
**Fix:**
1. Settings → Root Directory → `backend`
2. Redeploy

### **Issue 2: "Build Failed - No module named 'main'"**
**Cause:** Python can't find main.py
**Fix:**
1. Verify `PYTHONPATH=/app` is set in Variables
2. Verify Root Directory is set to `backend`
3. Check that `backend/main.py` exists in your repo

### **Issue 3: "Swiss Ephemeris not found"**
**Cause:** Ephemeris files not included
**Fix:**
1. Verify `backend/ephe/` folder is in your GitHub repo
2. Check `.gitignore` doesn't exclude `.se1` files
3. Redeploy after adding files

### **Issue 4: "Import Error: No module named 'modules'"**
**Cause:** Module imports failing
**Fix:**
1. Ensure `backend/modules/` folder exists
2. Ensure `backend/modules/__init__.py` exists
3. Check all module files are committed to GitHub

### **Issue 5: CORS Errors After Deployment**
**Cause:** CORS config not updated (but we already fixed this!)
**Status:** ✅ Already fixed in latest commit (e629eb9)

---

## 📊 Deployment Checklist

Before deploying, verify:

- [ ] Railway project exists or created
- [ ] GitHub repo connected: `sivaramanrajagopal/OpenAIAstroPrediction`
- [ ] Root Directory set to: **`backend`**
- [ ] Branch set to: **`main`**
- [ ] Environment variables added (especially `OPENAI_API_KEY`)
- [ ] Latest code pushed to GitHub
- [ ] Ephemeris files present in `backend/ephe/`
- [ ] All modules present in `backend/modules/`

---

## 🎯 Quick Command Reference

### Test Backend Health:
```bash
curl https://proactive-manifestation-production.up.railway.app/health
```

### Test Prediction Endpoint:
```bash
curl -X GET "https://proactive-manifestation-production.up.railway.app/predict?dob=1990-01-01&tob=12:00&lat=13.0827&lon=80.2707&tz_offset=5.5"
```

### View Railway Logs (via CLI):
```bash
# Install Railway CLI first
npm install -g @railway/cli

# Login and view logs
railway login
railway logs
```

---

## 🚀 After Successful Deployment

Once your backend is deployed and `/health` returns healthy:

1. **Test Frontend:** Visit https://aiastroprediction.vercel.app
2. **Fill in birth details** and click "Get Your Astrology Reading"
3. **Verify:** CORS errors should be gone!
4. **Expected:** Astrological data loads successfully

---

## 📞 Need Help?

If you encounter issues:

1. **Check Railway Logs:**
   - Railway Dashboard → Your Service → "Deployments" tab
   - Click on latest deployment → View build/runtime logs

2. **Check GitHub Sync:**
   - Ensure latest commit (e629eb9) is on main branch
   - Verify Railway is connected to the correct repo

3. **Verify Files in Repo:**
   - Go to: https://github.com/sivaramanrajagopal/OpenAIAstroPrediction/tree/main/backend
   - Confirm `main.py`, `requirements.txt`, `railway.toml` exist

---

## 🎉 Success Indicators

You'll know it's working when:
- ✅ `/health` endpoint returns `{"status": "healthy"}`
- ✅ Railway deployment shows "Active" status
- ✅ No CORS errors in browser console
- ✅ Frontend successfully fetches astrology data
- ✅ Build logs show: "Application startup complete"

---

**Ready to deploy? Start with Step 1!** 🚀

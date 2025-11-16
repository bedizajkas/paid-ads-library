# 🚀 GitHub Setup Guide

Follow these steps to deploy your Killer Paid Ads Library to GitHub!

---

## Step 1: Configure Git (One-time setup)

Run these commands in Terminal (replace with your info):

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

**Example:**
```bash
git config --global user.name "Benedek Zajkas"
git config --global user.email "benedek@example.com"
```

---

## Step 2: Create GitHub Repository

1. Go to **https://github.com** and sign in (or create account)

2. Click the **"+"** icon (top right) → **"New repository"**

3. Fill in:
   - **Repository name:** `paid-ads-library`
   - **Description:** "Killer Paid Ads Library - 91 AI-generated ad images"
   - **Visibility:** Public (required for free GitHub Pages)
   - **DO NOT** initialize with README (we already have one)

4. Click **"Create repository"**

5. **Copy the repository URL** - looks like:
   ```
   https://github.com/YOUR-USERNAME/paid-ads-library.git
   ```

---

## Step 3: Connect & Push to GitHub

Run these commands in Terminal (replace YOUR-USERNAME with your actual GitHub username):

```bash
cd "/Users/benedekzajkas/Coding/Paid ads"

# Add GitHub as remote
git remote add origin https://github.com/YOUR-USERNAME/paid-ads-library.git

# Rename branch to main (if needed)
git branch -M main

# Push code to GitHub
git push -u origin main
```

You may be prompted for GitHub credentials. Use a **Personal Access Token** instead of password:
- GitHub → Settings → Developer settings → Personal access tokens → Generate new token
- Give it "repo" permissions
- Copy the token and use it as your password

---

## Step 4: Enable GitHub Pages

1. Go to your repository on GitHub

2. Click **"Settings"** (top tab)

3. Click **"Pages"** (left sidebar)

4. Under "Source":
   - Select **"main"** branch
   - Keep folder as **"/ (root)"**
   - Click **"Save"**

5. Wait 1-2 minutes, then refresh the page

6. You'll see: **"Your site is live at https://YOUR-USERNAME.github.io/paid-ads-library"**

---

## 🎉 You're Done!

Your site is now live! Share the URL with anyone.

---

## 🔄 Making Updates Later

When you want to update images or make changes:

```bash
cd "/Users/benedekzajkas/Coding/Paid ads"

# Make your changes to index.html

# Commit and push
git add .
git commit -m "Updated ad images"
git push

# Changes will be live in 1-2 minutes!
```

---

## 🚀 OPTIONAL: Auto-Deploy with Vercel (Faster Updates)

For instant updates (10-20 seconds instead of 1-2 minutes):

1. Go to **https://vercel.com/new**

2. Click **"Import Git Repository"**

3. Sign in with GitHub

4. Select your `paid-ads-library` repository

5. Click **"Deploy"**

6. Done! You'll get a URL like: `https://paid-ads-library.vercel.app`

**Now every git push deploys in 10-20 seconds automatically!** ⚡

---

## 📝 Quick Reference

```bash
# Check status
git status

# Add all changes
git add .

# Commit changes
git commit -m "Your message here"

# Push to GitHub (auto-deploys!)
git push

# View remote URL
git remote -v
```

---

Need help? Let me know! 🙋‍♂️


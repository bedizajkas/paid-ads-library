# ⚡ Quick Start Guide

## 🎯 Share with Your Team in 3 Steps

### Step 1: Prepare the File (You do this once)

Open `image-viewer.html` in a code editor and find this section (around line 220):

```javascript
const PERMANENT_URLS = [
    // Paste your URLs here
];
```

Replace it with your 40 image URLs:

```javascript
const PERMANENT_URLS = [
    "https://your-url-1.png",
    "https://your-url-2.png",
    "https://your-url-3.png",
    // ... add all 40 URLs
];
```

**💡 Too tedious?** Use the helper script:
```bash
# Put your URLs in urls.txt (one per line), then run:
python convert-urls.py
# Copy the output and paste into the HTML!
```

### Step 2: Save the File

Press `Cmd+S` (Mac) or `Ctrl+S` (Windows)

### Step 3: Share!

**Pick any method:**

- 📧 **Email:** Attach the HTML file
- 💬 **Slack/Teams:** Upload the file
- ☁️ **Dropbox/Drive:** Share the link
- 🌐 **Host online:** Drag to https://app.netlify.com/drop

---

## 👥 Your Team's Experience

1. Receives the HTML file
2. Double-clicks to open in browser
3. **All 40 images load automatically!** ✨

**No setup, no passwords, no accounts needed!**

---

## 🔄 Update Images Later?

1. Edit the `PERMANENT_URLS` section again
2. Save
3. Re-share the file

That's it!

---

## 🌐 Want a Permanent URL Instead?

**Easiest:** Netlify (1 minute)
1. Go to https://app.netlify.com/drop
2. Drag and drop your HTML file
3. Get a URL like: `https://killer-ads.netlify.app`
4. Share that URL with your team!

**Updates?** Just re-drag the updated file to the same site.

---

## ❓ Questions?

See the full **`README.md`** or **`HOW-TO-SHARE.md`** for more options!


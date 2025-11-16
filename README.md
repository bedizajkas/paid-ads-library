# 🔥 Killer Paid Ads Library

A beautiful, branded viewer for your AI-generated ad images powered by Relevance AI.

![Relevance AI](https://img.shields.io/badge/Powered%20by-Relevance%20AI-5e72e4?style=for-the-badge)

---

## 📁 What's Included

- **`image-viewer.html`** - The main viewer (open in any browser!)
- **`HOW-TO-SHARE.md`** - Complete guide for sharing with your team
- **`convert-urls.py`** - Helper script to format URLs automatically
- **`EXAMPLE-urls-to-paste.txt`** - Template for pasting URLs

---

## 🚀 Quick Start (3 Ways to Use)

### Method 1: Manual Paste (Instant - No Setup)

1. Open `image-viewer.html` in any browser
2. Paste your image URLs (one per line) in the text box
3. Click "Load Images"
4. Done! ✨

**Perfect for:** Quick viewing, testing

---

### Method 2: Permanent Embedding (Best for Sharing)

1. Open `image-viewer.html` in a code editor
2. Find the `PERMANENT_URLS` section (around line 220)
3. Paste your URLs there like this:
   ```javascript
   const PERMANENT_URLS = [
       "https://your-image-1.png",
       "https://your-image-2.png",
       "https://your-image-3.png",
   ];
   ```
4. Save the file
5. Share with your team - images load automatically!

**Perfect for:** Sharing with team, presentations, archives

**💡 Pro tip:** Use the `convert-urls.py` script to format URLs automatically!

---

### Method 3: Host Online (Most Professional)

#### Option A: Netlify (1 minute)
1. Go to https://app.netlify.com/drop
2. Drag and drop `image-viewer.html`
3. Get instant URL → Share with team!

#### Option B: GitHub Pages (5 minutes)
See `HOW-TO-SHARE.md` for detailed instructions

**Perfect for:** Always-accessible URL, professional sharing, no file downloads

---

## 🛠️ Helper Tools

### Convert URLs Script

If you have URLs in a plain text file, use this script to format them:

```bash
# Create urls.txt with one URL per line, then run:
python convert-urls.py

# Or specify a custom file:
python convert-urls.py my-urls.txt
```

The script will output properly formatted JavaScript that you can copy-paste directly into the HTML!

---

## 📤 Sharing with Your Team

**For the simplest experience:**

1. Paste your 40 URLs into the `PERMANENT_URLS` section of the HTML
2. Save the file
3. Share via:
   - Email attachment
   - Slack/Teams upload
   - Dropbox/Google Drive link
   - AirDrop (Mac)

**Your team just needs to:**
- Download the HTML file
- Double-click to open in browser
- That's it! All images load automatically

See **`HOW-TO-SHARE.md`** for all sharing options!

---

## ✨ Features

- 🎨 **Beautiful branded design** with Relevance AI colors
- 📱 **Responsive grid** - works on any device
- 🔍 **Click to zoom** - full-screen image view
- ⚡ **Fast loading** - displays all images in parallel
- 🎯 **Zero dependencies** - just HTML, CSS, JavaScript
- 🔒 **Works offline** - no internet needed after images load
- 🎭 **Favicon included** - Relevance AI logo in browser tab

---

## 🔄 Workflow: Relevance AI → Viewer

### Current Workflow
```
Relevance AI generates 40 images
    ↓
Copy image URLs
    ↓
Paste into viewer
    ↓
View all images! ✨
```

### Want to Automate?

You can add a Python step in Relevance AI to automatically save URLs to a database. See these options:

1. **Airtable** - Visual database, simple API
2. **Google Sheets** - Everyone knows Sheets
3. **Supabase** - Full database + hosting
4. **Self-hosted** - Tiny Python server

Let me know if you want to set up automation!

---

## 🎨 Customization

Want to change the branding, colors, or add features? The HTML file is easy to customize:

- **Colors:** Search for `#5e72e4` (Relevance AI purple) and replace
- **Title:** Edit line 184-186 in the header section
- **Grid size:** Change `minmax(280px, 1fr)` on line ~105 for bigger/smaller images
- **Add password:** I can add simple password protection if needed!

---

## 💡 Tips & Tricks

### Multiple Campaigns
Save different versions for different campaigns:
- `ads-campaign-1.html`
- `ads-campaign-2.html`
- `ads-holiday-2025.html`

Each file has different images embedded!

### Quick Updates
To change images in a shared file:
1. Edit the `PERMANENT_URLS` array
2. Save
3. Re-share the file (or re-upload to Netlify/GitHub)

### Batch Naming
Add comments in your URL array to organize:
```javascript
const PERMANENT_URLS = [
    // Facebook Ads
    "https://image1.png",
    "https://image2.png",
    
    // Instagram Ads
    "https://image3.png",
    "https://image4.png",
];
```

---

## 🐛 Troubleshooting

**Images not loading?**
- Check that URLs are publicly accessible
- Make sure URLs start with `http://` or `https://`
- Try opening a URL directly in your browser to test

**JavaScript errors?**
- Make sure each URL has quotes: `"url"`
- Make sure each URL (except last) has a comma: `"url",`
- Check the browser console (F12) for error details

**File won't open?**
- Make sure the file extension is `.html` not `.txt`
- Try right-click → Open With → Chrome/Firefox/Safari

---

## 📞 Need Help?

If you need assistance with:
- Setting up automation with Relevance AI
- Hosting the viewer online
- Custom features or branding
- Anything else!

Just ask! 🚀

---

## 📄 License

Free to use and customize for your team!

---

**Made with 💜 by Relevance AI**


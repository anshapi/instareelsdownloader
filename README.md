




markdown
# 📸 Instagram Reels Downloader API

An easy-to-use API that extracts **download URL**, **caption**, and **thumbnail** from **public Instagram Reels** using `yt-dlp`, built with Python Flask.

---

## 🚀 Features

- 🔗 Get **direct download URL** of Instagram Reels (public only, no cookies required)
- 📝 Fetch **caption** (title/description)
- 🖼️ Get **thumbnail** URL
- ⚡ Fast & lightweight
- 🌐 Deployable on any Python server or service like Render, Railway, Vercel (via Flask adapter)



## 📦 Requirements

```bash
pip install flask yt-dlp
```

---

## 🔧 How to Use

### 1. Start the server

```bash
python instagram_reels_api.py
```

### 2. Make a GET request:

```
http://localhost:5000/api/instagram/reel?url=https://www.instagram.com/reel/<REEL_ID>/
```

### ✅ Example Response:

```json
{
  "status": "success",
  "video_url": "https://instagram.cdn/....mp4",
  "caption": "My awesome reel ✨",
  "thumbnail": "https://instagram.cdn/....jpg"
}
```

---

## 🧠 How It Works

This API uses the powerful [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) library to extract metadata and media links from publicly available Instagram Reel URLs.

---

## 🛑 Limitations

- ❌ Doesn't support **private** or **login-required** reels (use cookies if needed)
- ⚠️ Instagram may rate-limit or block IPs for scraping at scale — use responsibly.

---

## 👨‍💻 Developer

**Made with ❤️ by [AnshAPI](https://t.me/AnshAPI) on Telegram**

- ✨ Telegram Bot, API, & Python Projects Expert
- 🔗 Custom tools, bots, and scraping APIs

---

## 📜 License

This project is free to use and modify. Credits are appreciated.

```

---

Let me know if you also want:
- 🔄 A **Vercel deploy-ready version**
- 🌐 A **web UI**
- 📁 A **ZIP package**

I'll prepare them quickly.

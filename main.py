from flask import Flask, request, jsonify
import yt_dlp

app = Flask(__name__)

def get_instagram_reel_info(reel_url):
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
        'force_generic_extractor': False,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(reel_url, download=False)
            video_url = info.get('url')
            title = info.get('title')
            thumbnail = info.get('thumbnail')
            return {
                'status': 'success',
                'video_url': video_url,
                'caption': title,
                'thumbnail': thumbnail
            }
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

@app.route('/api/instagram/reel', methods=['GET'])
def instagram_reel_api():
    reel_url = request.args.get('url')
    if not reel_url:
        return jsonify({'status': 'error', 'message': 'Missing "url" parameter'}), 400

    result = get_instagram_reel_info(reel_url)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

from flask import Flask, render_template, request, jsonify
from modules.browser import Browser
from threading import Thread
import time

is_browser_start = False
player = None

def _start_browser_player():
    global player
    player = Browser()

Thread(target=_start_browser_player, daemon=True).start()
time.sleep(10)

app = Flask(__name__)

@app.route('/')
def index():
    track_name, group_name, image_url = player.get_track_info()
    
    return render_template('index.html', track_name=track_name, group_name=group_name, image_url=image_url)

@app.route('/music/<method>')
def change_music(method):
    key_list = ['title', 'subtitle', 'img_link']
    match method:
        case 'next':
            player.next()

            time.sleep(1)
            result = {}
            for idx, name in enumerate(player.get_track_info()):
                result[key_list[idx]] = name
            return jsonify(result)
        
        case 'back':
            player.back()
            
            time.sleep(1)
            result = {}
            for idx, name in enumerate(player.get_track_info()):
                result[key_list[idx]] = name
            return jsonify(result)
        
        case 'play':
            player.play()
            
            result = {}
            for idx, name in enumerate(player.get_track_info()):
                result[key_list[idx]] = name
            return jsonify(result)
        
        case 'info':
            result = {}
            for idx, name in enumerate(player.get_track_info()):
                result[key_list[idx]] = name
            return jsonify(result)

    return

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)
"use strict";

const track_image = document.getElementById('track_image');
const track_title = document.getElementById('title');
const track_group = document.getElementById('subtitle');

const audio_player = document.getElementById('audio_player');

function send_request(method) {
    let url = window.origin + '/music/' + method;

    fetch(url)
        .then(response => {
            if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })

        .then(data => {
            // console.log('Data received:', data);
            // console.log(data);

            track_image.src = data['img_link'];
            track_title.innerText = data['title'];
            track_group.innerText = data['subtitle'];

            document.title = data['title'];

            navigator.mediaSession.metadata = new MediaMetadata({
                title: data['title'],
                artist: data['subtitle'],
                artwork: [
                    {
                    src: data['img_link'],
                    sizes: "400x400",
                    type: "image/jpg",
                    }
                ],
            })

            audio_player.load();
            audio_player.play();
        })

        .catch(error => {
            console.error('Fetch error:', error);
    });
}

// if ("mediaSession" in navigator) {
//     navigator.mediaSession.metadata = new MediaMetadata({
//     title: "Unforgettable",
//     artist: "Nat King Cole",
//     album: "The Ultimate Collection (Remastered)",
//     artwork: [
//         {
//         src: "https://dummyimage.com/96x96",
//         sizes: "400x400",
//         type: "image/jpg",
//         }
//     ],
// })};

navigator.mediaSession.setActionHandler(
    'nexttrack',
    () => { send_request('next'); }
);

navigator.mediaSession.setActionHandler(
    'previoustrack',
    () => { send_request('back'); }
);

navigator.mediaSession.setActionHandler(
    'play',
    () => { send_request('play'); }
);

navigator.mediaSession.setActionHandler(
    'pause',
    () => { send_request('play'); }
);

setInterval(() => {
    send_request('info');
}, 30000)
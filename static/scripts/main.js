"use strict";

const track_image = document.getElementById('track_image');
const track_title = document.getElementById('title');
const track_group = document.getElementById('subtitle');

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
        })

        .catch(error => {
            console.error('Fetch error:', error);
    });
}

setInterval(() => {
    send_request('info');
}, 30000)
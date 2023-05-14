var map = L.map('map').setView([47.218371, -1.553621], 4);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

    L.marker([47.2249, -1.54537]).addTo(map)
    .bindPopup("LGT Livet - CPGE - PTSI")
    .openPopup();
    
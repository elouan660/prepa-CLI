var map = L.map('map').setView([47.218371, -1.553621], 4);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

    L.marker([47.2189, -1.5448]).addTo(map)
    .bindPopup("Lycée général Clemenceau - CPGE - MP2I")
    .openPopup();
    
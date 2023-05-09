var map = L.map('map').setView([47.218371, -1.553621], 4);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

    L.marker([47.2225, -1.55535]).addTo(map)
    .bindPopup("LGT Saint-Stanislas - CPGE - MPSI")
    .openPopup();
    
    L.marker([47.2189, -1.5448]).addTo(map)
    .bindPopup("Lycée général Clemenceau - CPGE - MPSI")
    .openPopup();
    
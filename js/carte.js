var map = L.map('map').setView([47.218371, -1.553621], 4);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

    L.marker([45.5638, 5.93454]).addTo(map)
    .bindPopup("Lycée Monge - CPGE - TSI - (en 3 ans, destinée aux bacs professionnels)")
    .openPopup();
    
    L.marker([46.6756, 4.37252]).addTo(map)
    .bindPopup("Lycée Henri Parriat - CPGE - TSI - (en 3 ans, destinée aux bacs professionnels)")
    .openPopup();
    
    L.marker([43.8344, 4.37175]).addTo(map)
    .bindPopup("Lycée Emmanuel d'Alzon - CPGE - TSI - (en 3 ans, destinée aux bacs professionnels)")
    .openPopup();
    
    L.marker([49.851, 3.30076]).addTo(map)
    .bindPopup("Lycée Pierre de La Ramee - CPGE - PCSI")
    .openPopup();
    
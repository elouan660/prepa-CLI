var map = L.map('map').setView([47.218371, -1.553621], 4);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

    L.marker([-20.8879, 55.4693]).addTo(map)
    .bindPopup("Lycée Leconte de Lisle - CPGE - MP2I")
    .openPopup();
    
    L.marker([-21.2741, 55.5199]).addTo(map)
    .bindPopup("Lycée Roland Garros - CPGE - PCSI")
    .openPopup();
    
    L.marker([-21.3382, 55.4797]).addTo(map)
    .bindPopup("Lycée Catholique St Charles - CPGE - MPSI")
    .openPopup();
    
    L.marker([-21.0397, 55.7156]).addTo(map)
    .bindPopup("Lycée Amiral Pierre Bouvet - CPGE - TSI")
    .openPopup();
    
    L.marker([-20.8879, 55.4693]).addTo(map)
    .bindPopup("Lycée Leconte de Lisle - CPGE - MPSI")
    .openPopup();
    
    L.marker([-21.2741, 55.5199]).addTo(map)
    .bindPopup("Lycée Roland Garros - CPGE - BCPST")
    .openPopup();
    
    L.marker([-20.8879, 55.4693]).addTo(map)
    .bindPopup("Lycée Leconte de Lisle - CPGE - PCSI")
    .openPopup();
    
    L.marker([-20.8903, 55.4657]).addTo(map)
    .bindPopup("Lycée Lislet Geoffroy - CPGE - PTSI")
    .openPopup();
    
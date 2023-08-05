var map = L.map('mapa').setView([-1.037300, -79.458696], 10);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);


map.on('click', function(e) {
    let lng=document.getElementById("lng");
    let lat=document.getElementById("lat");
    alert(e.latlng);
    L.marker([e.latlng.lat,e.latlng.lng]).addTo(map)
    .bindPopup('Jhon')
    .openPopup();
    console.log(e);
    lng.value=e.latlng.lng
    lat.value=e.latlng.lat
} );
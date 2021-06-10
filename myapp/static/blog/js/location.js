var map_35809f388aae40589af943d6540f3e82 = L.map(
    "map_35809f388aae40589af943d6540f3e82",
    {
        center: [40.359673, 71.27584],
        crs: L.CRS.EPSG3857,
        zoom: 18,
        zoomControl: true,
        preferCanvas: false,
    }
);

var tile_layer_96c8ed05a6ea453c85a1a1b2f11b5b47 = L.tileLayer(
    "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
    {"attribution": "Data by \u0026copy; \u003ca href=\"http://openstreetmap.org\"\u003eOpenStreetMap\u003c/a\u003e, under \u003ca href=\"http://www.openstreetmap.org/copyright\"\u003eODbL\u003c/a\u003e.", "detectRetina": false, "maxNativeZoom": 18, "maxZoom": 18, "minZoom": 0, "noWrap": false, "opacity": 1, "subdomains": "abc", "tms": false}
).addTo(map_35809f388aae40589af943d6540f3e82);


var feature_group_9d5d4d796a17401c9f852c32425cc895 = L.featureGroup(
    {}
).addTo(map_35809f388aae40589af943d6540f3e82);


var marker_62926f4068cf4c608b54fe3e81455d08 = L.marker(
    [40.359673, 71.27584],
    {}
).addTo(feature_group_9d5d4d796a17401c9f852c32425cc895);


var icon_dbc68943e05b4c5292cf63a309686022 = L.AwesomeMarkers.icon(
    {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "white", "markerColor": "green", "prefix": "glyphicon"}
);
marker_62926f4068cf4c608b54fe3e81455d08.setIcon(icon_dbc68943e05b4c5292cf63a309686022);


var popup_f463bfa0d0624168899a63bccc435d53 = L.popup({"maxWidth": "100%"});


var html_07cee1dc282a4f23bbbf9161ee005b37 = $(`<div id="html_07cee1dc282a4f23bbbf9161ee005b37" style="width: 100.0%; height: 100.0%;">Rishton tuman Davlat xizmatlari markazi</div>`)[0];
popup_f463bfa0d0624168899a63bccc435d53.setContent(html_07cee1dc282a4f23bbbf9161ee005b37);


marker_62926f4068cf4c608b54fe3e81455d08.bindPopup(popup_f463bfa0d0624168899a63bccc435d53)
;
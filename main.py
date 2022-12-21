from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

contents = {
    "open":"Otwórz jeden z zapisanych projektów:",
    "save":"Zapisz projekt jako plik konfiguracyjny GisPortalu:",
    "export":"Wyeksportuj plik konfiguracyjny i kontynuuj pracę na innym urządzeniu:",
    "settings":"Skonfiguruj program do własnych potrzeb:",
    "wms":"Wybierz jedno ze źródeł WMS lub skonfiguruj nowe:",
    "map":"Wybierz typ mapy odpowiedni do potrzeb projektu:",
    "raster":"Wybierz z dostępnych rastrów lub wgraj nowy w formacie .tiff:",
    "vector":"Wybierz z dostępnych warstw lub dodaj nową w formacie .geojson:"
}

forms = {
    "open":"undefined",
    "save":"undefined",
    "export":"undefined",
    "settings":"undefined",
    "wms":"undefined",
    "map":"""
<input type="radio" id="map0" name="map" onchange="setMapUrl('');"/><label for="map0">Brak mapy</label></br>
<input type="radio" id="map1" name="map" onchange="setMapUrl('https://tile.openstreetmap.org/{z}/{x}/{y}.png');"/><label for="map1">Open Street Map - Mapnik</label></br>
<input type="radio" id="map2" name="map" onchange="setMapUrl('https://{s}.tile.openstreetmap.de/{z}/{x}/{y}.png');"/><label for="map2">Open Street Map - DE</label></br>
<input type="radio" id="map3" name="map" onchange="setMapUrl('https://tile.osm.ch/switzerland/{z}/{x}/{y}.png');"/><label for="map3">Open Street Map - CH</label></br>
<input type="radio" id="map4" name="map" onchange="setMapUrl('https://{s}.tile.openstreetmap.fr/osmfr/{z}/{x}/{y}.png');"/><label for="map4">Open Street Map - FR</label></br>
<input type="radio" id="map5" name="map" onchange="setMapUrl('https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png');"/><label for="map5">Open Street Map - HOT</label></br>
<input type="radio" id="map6" name="map" onchange="setMapUrl('https://tile.openstreetmap.bzh/br/{z}/{x}/{y}.png');"/><label for="map6">Open Street Map - BZH</label></br>
<input type="radio" id="map7" name="map" onchange="setMapUrl('https://tileserver.memomaps.de/tilegen/{z}/{x}/{y}.png');"/><label for="map7">OPNV Karte</label></br>
<input type="radio" id="map8" name="map" onchange="setMapUrl('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png');"/><label for="map8">Open Topo Map</label></br>
<input type="radio" id="map9" name="map" onchange="setMapUrl('https://{s}.tile-cyclosm.openstreetmap.fr/cyclosm/{z}/{x}/{y}.png');"/><label for="map9">Cycl OSM</label></br>
<input type="radio" id="map10" name="map" onchange="setMapUrl('https://stamen-tiles-{s}.a.ssl.fastly.net/toner/{z}/{x}/{y}{r}.png');"/><label for="map10">Stamen Toner</label></br>
<input type="radio" id="map11" name="map" onchange="setMapUrl('https://stamen-tiles-{s}.a.ssl.fastly.net/toner-background/{z}/{x}/{y}{r}.png');"/><label for="map11">Stamen Toner Background</label></br>
<input type="radio" id="map12" name="map" onchange="setMapUrl('https://stamen-tiles-{s}.a.ssl.fastly.net/toner-lite/{z}/{x}/{y}{r}.png');"/><label for="map12">Stamen Toner Lite</label></br>
<input type="radio" id="map14" name="map" onchange="setMapUrl('https://stamen-tiles-{s}.a.ssl.fastly.net/watercolor/{z}/{x}/{y}.png');"/><label for="map14">Stamen Water Color</label></br>
<input type="radio" id="map15" name="map" onchange="setMapUrl('https://stamen-tiles-{s}.a.ssl.fastly.net/terrain/{z}/{x}/{y}{r}.png');"/><label for="map15">Stamen Terrain</label></br>
<input type="radio" id="map16" name="map" onchange="setMapUrl('https://stamen-tiles-{s}.a.ssl.fastly.net/terrain-background/{z}/{x}/{y}{r}.png');"/><label for="map16">Stamen Terrain Background</label></br>
<input type="radio" id="map17" name="map" onchange="setMapUrl('https://stamen-tiles-{s}.a.ssl.fastly.net/terrain-labels/{z}/{x}/{y}{r}.png');"/><label for="map17">Stamen Terrain Labels</label></br>
<input type="radio" id="map18" name="map" onchange="setMapUrl('https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}');"/><label for="map18">ESRI World Street Map</label></br>
<input type="radio" id="map19" name="map" onchange="setMapUrl('https://server.arcgisonline.com/ArcGIS/rest/services/Specialty/DeLorme_World_Base_Map/MapServer/tile/{z}/{y}/{x}');"/><label for="map19">ESRI DeLorme</label></br>
<input type="radio" id="map20" name="map" onchange="setMapUrl('https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}');"/><label for="map20">ESRI World Topo Map</label></br>
<input type="radio" id="map21" name="map" onchange="setMapUrl('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}');"/><label for="map21">ESRI World Imagery</label></br>
<input type="radio" id="map22" name="map" onchange="setMapUrl('https://server.arcgisonline.com/ArcGIS/rest/services/World_Terrain_Base/MapServer/tile/{z}/{y}/{x}');"/><label for="map22">ESRI World Terrain</label></br>
<input type="radio" id="map23" name="map" onchange="setMapUrl('https://server.arcgisonline.com/ArcGIS/rest/services/World_Shaded_Relief/MapServer/tile/{z}/{y}/{x}');"/><label for="map23">ESRI World Shaded Relief</label></br>
<input type="radio" id="map24" name="map" onchange="setMapUrl('https://server.arcgisonline.com/ArcGIS/rest/services/World_Physical_Map/MapServer/tile/{z}/{y}/{x}');"/><label for="map24">ESRI World Physical</label></br>
<input type="radio" id="map25" name="map" onchange="setMapUrl('https://server.arcgisonline.com/ArcGIS/rest/services/NatGeo_World_Map/MapServer/tile/{z}/{y}/{x}');"/><label for="map25">ESRI NatGeo World Map</label></br>
<input type="radio" id="map26" name="map" onchange="setMapUrl('http://tile.mtbmap.cz/mtbmap_tiles/{z}/{x}/{y}.png');"/><label for="map26">Mtb Map</label></br>
<input type="radio" id="map27" name="map" onchange="setMapUrl('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png');"/><label for="map27">Carto DB Positron</label></br>
<input type="radio" id="map28" name="map" onchange="setMapUrl('https://{s}.basemaps.cartocdn.com/light_nolabels/{z}/{x}/{y}{r}.png');"/><label for="map28">Carto DB Positron No Labels</label></br>
<input type="radio" id="map29" name="map" onchange="setMapUrl('https://{s}.basemaps.cartocdn.com/light_only_labels/{z}/{x}/{y}{r}.png');"/><label for="map29">Carto DB Positron Only Labels</label></br>
<input type="radio" id="map30" name="map" onchange="setMapUrl('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png');"/><label for="map30">Carto DB Dark Matter</label></br>
<input type="radio" id="map31" name="map" onchange="setMapUrl('https://{s}.basemaps.cartocdn.com/dark_nolabels/{z}/{x}/{y}{r}.png');"/><label for="map31">Carto DB Dark Matter No Labels</label></br>
<input type="radio" id="map32" name="map" onchange="setMapUrl('https://{s}.basemaps.cartocdn.com/dark_only_labels/{z}/{x}/{y}{r}.png');"/><label for="map32">Carto DB Dark Matter Only Labels</label></br>
<input type="radio" id="map33" name="map" onchange="setMapUrl('https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png');"/><label for="map33">Carto DB Voyager</label></br>
<input type="radio" id="map34" name="map" onchange="setMapUrl('https://{s}.basemaps.cartocdn.com/rastertiles/voyager_nolabels/{z}/{x}/{y}{r}.png');"/><label for="map34">Carto DB Voyager No Labels</label></br>
<input type="radio" id="map35" name="map" onchange="setMapUrl('https://{s}.basemaps.cartocdn.com/rastertiles/voyager_only_labels/{z}/{x}/{y}{r}.png');"/><label for="map35">Carto DB Voyager Only Labels</label></br>
<input type="radio" id="map36" name="map" onchange="setMapUrl('https://map1.vis.earthdata.nasa.gov/wmts-webmerc/MODIS_Terra_CorrectedReflectance_TrueColor/default//GoogleMapsCompatible_Level9/{z}/{y}/{x}.jpg');"/><label for="map36">NASAGIBS Modis Terra True Color CR</label></br>
<input type="radio" id="map37" name="map" onchange="setMapUrl('https://map1.vis.earthdata.nasa.gov/wmts-webmerc/MODIS_Terra_CorrectedReflectance_Bands367/default//GoogleMapsCompatible_Level9/{z}/{y}/{x}.jpg');"/><label for="map37">NASAGIBS Modis Terra Bands 367 CR</label></br>
<input type="radio" id="map38" name="map" onchange="setMapUrl('https://map1.vis.earthdata.nasa.gov/wmts-webmerc/VIIRS_CityLights_2012/default//GoogleMapsCompatible_Level8/{z}/{y}/{x}.jpg');"/><label for="map38">NASAGIBS Viirs Earth At Night 2012</label></br>
<input type="radio" id="map39" name="map" onchange="setMapUrl('https://basemap.nationalmap.gov/arcgis/rest/services/USGSTopo/MapServer/tile/{z}/{y}/{x}');"/><label for="map39">USGS US Topo</label></br>
<input type="radio" id="map40" name="map" onchange="setMapUrl('https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}');"/><label for="map40">USGS US Imagery</label></br>
<input type="radio" id="map41" name="map" onchange="setMapUrl('https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryTopo/MapServer/tile/{z}/{y}/{x}');"/><label for="map41">USGS US Imagery Topo</label></br>
    """,
    "raster":"undefined",
    "vector":"undefined",
}

@app.get("/test")
async def root():
    return {"status":"connected"}

@app.get("/{window}")
async def root(window):
    return {"content": contents[window],"form":forms[window]}
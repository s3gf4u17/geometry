import {MyWindow} from "./MyClasses";
import L from "leaflet";
import GeoRasterLayer from "georaster-layer-for-leaflet";
import parseGeoraster from "georaster";

// async function sendFile(){
//   const file = await document.getElementById("geojson").files;
//   const formData = await new FormData();
//   await formData.append("file",file[0]);
//   await fetch("http://localhost:8000/geojson/",{
//     "method":"POST",
//     "body":formData
//   }).then(res=>res.json()).then(data=>alert(data.status))
// }

function baseMap(map){
  var sources = [
    {name:"Brak warstwy",url:"",attribution:"GisPortal",maxZoom:20},
    {name:"Open Street Maps Mapnik",url:"https://tile.openstreetmap.org/{z}/{x}/{y}.png",attribution:'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',maxZoom:19},
    {name:'Open Street Maps DE',url:'https://{s}.tile.openstreetmap.de/{z}/{x}/{y}.png',attribution:'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',maxZoom:18},
    {name:'Open Street Maps France',url:'https://{s}.tile.openstreetmap.fr/osmfr/{z}/{x}/{y}.png',attribution:'&copy; OpenStreetMap France | &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',maxZoom:20},
    {name:'Open Street Maps Hot',url:'https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png',attribution:'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Tiles style by <a href="https://www.hotosm.org/" target="_blank">Humanitarian OpenStreetMap Team</a> hosted by <a href="https://openstreetmap.fr/" target="_blank">OpenStreetMap France</a>',maxZoom:19},
    {name:'OPNV Karte',url:'https://tileserver.memomaps.de/tilegen/{z}/{x}/{y}.png',attribution:'Map <a href="https://memomaps.de/">memomaps.de</a> <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',maxZoom:18},
    {name:'Open Topo Map',url:'https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png',attribution:'Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)',maxZoom:17},
    {name:'Cycl OSM',url:'https://{s}.tile-cyclosm.openstreetmap.fr/cyclosm/{z}/{x}/{y}.png',attribution:'<a href="https://github.com/cyclosm/cyclosm-cartocss-style/releases" title="CyclOSM - Open Bicycle render">CyclOSM</a> | Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',maxZoom:20},
    {name:'ESRI World Street Map',url:'https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}',attribution:'Tiles &copy; Esri &mdash; Source: Esri, DeLorme, NAVTEQ, USGS, Intermap, iPC, NRCAN, Esri Japan, METI, Esri China (Hong Kong), Esri (Thailand), TomTom, 2012',maxZoom:20},
    {name:'ESRI DeLorme',url:'https://server.arcgisonline.com/ArcGIS/rest/services/Specialty/DeLorme_World_Base_Map/MapServer/tile/{z}/{y}/{x}',attribution:'Tiles &copy; Esri &mdash; Copyright: &copy;2012 DeLorme',maxZoom:11},
    {name:'ESRI World Topo Map',url:'https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}',attribution:'Tiles &copy; Esri &mdash; Esri, DeLorme, NAVTEQ, TomTom, Intermap, iPC, USGS, FAO, NPS, NRCAN, GeoBase, Kadaster NL, Ordnance Survey, Esri Japan, METI, Esri China (Hong Kong), and the GIS User Community',maxZoom:20},
    {name:'ESRI World Imagery',url:'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',attribution:'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community',maxZoom:20},
    {name:'ESRI World Terrain',url:'https://server.arcgisonline.com/ArcGIS/rest/services/World_Terrain_Base/MapServer/tile/{z}/{y}/{x}',attribution:'Tiles &copy; Esri &mdash; Source: USGS, Esri, TANA, DeLorme, and NPS',maxZoom:13},
    {name:'ESRI NatGeoWorld Map',url:'https://server.arcgisonline.com/ArcGIS/rest/services/NatGeo_World_Map/MapServer/tile/{z}/{y}/{x}',attribution:'Tiles &copy; Esri &mdash; National Geographic, Esri, DeLorme, NAVTEQ, UNEP-WCMC, USGS, NASA, ESA, METI, NRCAN, GEBCO, NOAA, iPC',maxZoom:16},
    {name:'ESRI World Gray Canvas',url:'https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/{z}/{y}/{x}',attribution:'Tiles &copy; Esri &mdash; Esri, DeLorme, NAVTEQ',maxZoom:16},
    {name:'Carto DB Voyager No Labels',url:'https://{s}.basemaps.cartocdn.com/rastertiles/voyager_nolabels/{z}/{x}/{y}{r}.png',attribution:'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',maxZoom:20},
    {name:'Carto DB Voyager With Labels',url:'https://{s}.basemaps.cartocdn.com/rastertiles/voyager_labels_under/{z}/{x}/{y}{r}.png',attribution:'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',maxZoom:20},
    {name:'USGS US Topo',url:'https://basemap.nationalmap.gov/arcgis/rest/services/USGSTopo/MapServer/tile/{z}/{y}/{x}',attribution:'Tiles courtesy of the <a href="https://usgs.gov/">U.S. Geological Survey</a>',maxZoom:20},
    {name:'USGS US Imagery',url:'https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}',attribution:'Tiles courtesy of the <a href="https://usgs.gov/">U.S. Geological Survey</a>',maxZoom:20},
  ]
  var content = document.createElement("div");
  content.classList.add("window-content");
  for(let i = 0;i< sources.length;i++){
    var source = sources[i];
    var inp = document.createElement("input");
    inp.type = "radio";
    inp.id = "inp"+i;
    inp.name = "baseMap";
    content.appendChild(inp);
    inp.source = source;
    inp.addEventListener("click",(e)=>{
      map.eachLayer(function(layer){if(layer.options.id==="tilelayer"){map.removeLayer(layer);}});
      L.tileLayer(e.currentTarget.source.url,{id:"tilelayer",attribution:e.currentTarget.source.attribution,maxZoom:e.currentTarget.source.maxZoom}).addTo(map)
    });
    var lab = document.createElement("label");
    lab.setAttribute("for","inp"+i);
    lab.innerHTML = source.name;
    content.appendChild(lab)
    var br = document.createElement("br");
    content.appendChild(br);
  }
  new MyWindow("Mapa podstawowa",content);
}

async function rasterLayer(map){
  var content = document.createElement("div");
  var but = document.createElement("button");
  but.type = "button";
  but.id = "upload-button";
  but.innerHTML = "Przeslij";
  content.appendChild(but);
  but.disabled = true;
  but.addEventListener("click",async ()=>{
    const file = await document.getElementById("geotiff").files;
    const formData = await new FormData();
    await formData.append("file",file[0]);
    await fetch("http://localhost:8000/geotiff/",{method:"POST",body:formData,mode:"cors"}).then(res=>res.json()).then(data=>rasterLayer(map));
  })
  var inp = document.createElement("input");
  inp.type="file";
  inp.id = "geotiff";
  inp.accept = ".geotiff,.tif";
  inp.addEventListener("change",()=>{but.disabled=false;})
  content.appendChild(inp);
  var br = document.createElement("br");
  content.appendChild(br);
  await fetch("http://localhost:8000/geotiff/").then(res=>res.json()).then((data)=>{
    for (let i = 0; i < data.layers.length;i++){
      var elm = document.createElement("input");
      elm.type="radio";
      elm.id = "ras"+i;
      content.appendChild(elm);
      var lab = document.createElement("label");
      lab.innerHTML = data.layers[i];
      lab.setAttribute("for","ras"+i);
      content.appendChild(lab);
      var br = document.createElement("br");
      content.appendChild(br);
      elm.addEventListener("change",async ()=>{
        await fetch("http://localhost/data.geotiff/"+data.layers[i])
        .then(response=>response.arrayBuffer()).then(arrayBuffer=>{parseGeoraster(arrayBuffer).then(raster=>{
          raster.projection = 4326;
          var layer = new GeoRasterLayer({georaster:raster,opacity:0.6});
          layer.addTo(map);
        })})
      })
    }
  });
  new MyWindow("Warstwy rastrowe",content);
}

function PrimaryBar({map}) {
    return (
      <div className="PrimaryBar">
        <div className="BarButton" onClick={()=>{baseMap(map)}}><i className="fa-solid fa-chess-board"></i> Mapa podstawowa</div>
        <div className="BarButton" onClick={()=>{rasterLayer(map)}}><i className="fa-solid fa-image"></i> Warstwy rastrowe</div>
        <div className="BarButton"><i className="fa-solid fa-vector-square"></i> Warstwy wektorowe</div>
        <div className="BarButton"><i className="fa-solid fa-map"></i> WMS</div>
        {/* <input className="BarButton" id="geojson" type="file" accept=".geojson"/>
        <button className="BarButton" type="button" onClick={sendFile}>przeslij</button> */}
      </div>
    );
  }
  
  export default PrimaryBar;
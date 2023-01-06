package router

import "net/http"
import "new-gis-portal/model"
import "encoding/json"
import "io/ioutil"

func ApiManual(w http.ResponseWriter, r *http.Request) {
	http.ServeFile(w,r,"html/api.html")
}

func GeojsonLayers(w http.ResponseWriter, r *http.Request) {
	layers := []model.GeoJsonLayer{}
	files,_:=ioutil.ReadDir("data/geojson")
	for _,file := range files {
		if !file.IsDir() {layers = append(layers,model.GeoJsonLayer{file.Name()})}
	}
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(layers)
}

func GeotiffLayers(w http.ResponseWriter, r *http.Request) {
	layers := []model.GeoTiffLayer{}
	files,_:=ioutil.ReadDir("data/geotiff")
	for _,file := range files {
		if !file.IsDir() {layers = append(layers,model.GeoTiffLayer{file.Name()})}
	}
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(layers)
}
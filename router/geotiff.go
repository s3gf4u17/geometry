package router

import "net/http"
import "new-gis-portal/model"
import "encoding/json"
import "io/ioutil"

func isValid(source string) bool {
	files,_:=ioutil.ReadDir("data/geojson")
	for _,file := range files {
		if !file.IsDir() && file.Name() == source {return true}
	}
	return false
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
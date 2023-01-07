package router

import "net/http"
import "new-gis-portal/model"
import "encoding/json"
import "io/ioutil"
import "strings"
import "fmt"
import "os"
import "io"

func isValid(source string) bool {
	files,_:=ioutil.ReadDir("data/geotiff")
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

func GeotiffLayers(w http.ResponseWriter, r *http.Request) {
	source := strings.TrimPrefix(r.URL.Path, "/api/geotiff/")
	method := r.Method
	if source == "" && method == "GET" { // get all available layers
		layers:=[]model.GeoTiffLayer{}
		files,_:=ioutil.ReadDir("data/geotiff")
		for _,file := range files {if !file.IsDir() {layers=append(layers,model.GeoTiffLayer{file.Name()})}}
		w.Header().Set("Content-Type", "application/json")
		json.NewEncoder(w).Encode(layers)
	} else if source == "" && method == "POST" { // create new geotiff layer
		file,header,_:=r.FormFile("file")
		fmt.Printf("%s",header.Filename)
		ondisk,_:=os.Create("data/geotiff/"+header.Filename)
		io.Copy(ondisk,file)
	} else if source != "" && method == "GET" { // read geotiff layer
		var valid bool = isValid(source)
		if valid {http.ServeFile(w,r,"data/geotiff/"+source)}
	}
}
package router

import "net/http"
import "new-gis-portal/model"
import "encoding/json"
import "io/ioutil"
import "strings"
import "fmt"
import "os"
import "io"

func isValidGeojson(source string) bool {
	files,_:=ioutil.ReadDir("data/geojson")
	for _,file := range files {
		if !file.IsDir() && file.Name() == source {return true}
	}
	return false
}

func GeojsonLayers(w http.ResponseWriter, r *http.Request) {
	source := strings.TrimPrefix(r.URL.Path, "/api/geojson/")
	method := r.Method
	if source == "" && method == "GET" { // get all available layers
		layers:=[]model.GeoJsonLayer{}
		files,_:=ioutil.ReadDir("data/geojson")
		for _,file := range files {if !file.IsDir() {layers=append(layers,model.GeoJsonLayer{file.Name()})}}
		w.Header().Set("Content-Type", "application/json")
		json.NewEncoder(w).Encode(layers)
	} else if source == "" && method == "POST" { // create new geojson layer
		file,header,_:=r.FormFile("file")
		fmt.Printf("%s",header.Filename)
		ondisk,_:=os.Create("data/geojson/"+header.Filename)
		io.Copy(ondisk,file)
	} else if source != "" && method == "GET" { // read geojson layer
		var valid bool = isValidGeojson(source)
		if valid {http.ServeFile(w,r,"data/geojson/"+source)}
	}
}
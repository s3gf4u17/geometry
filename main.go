package main

import "net/http"
import "new-gis-portal/router"

func main() {
	http.HandleFunc("/api/geojson/",router.GeojsonLayers)
	http.HandleFunc("/api/geotiff/",router.GeotiffLayers)
	http.HandleFunc("/api/",router.ApiManual)
	http.ListenAndServe("localhost:8000",nil)
}
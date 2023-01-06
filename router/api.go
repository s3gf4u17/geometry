package router

import "net/http"
// import "io/ioutil"

func ApiManual(w http.ResponseWriter, r *http.Request) {
	http.ServeFile(w,r,"html/api/index.html")
}
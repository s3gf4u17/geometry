package router

import "net/http"
// import "io/ioutil"

func ApiManual(w http.ResponseWriter, r *http.Request) {
	if r.URL.Path == "/api/" {
		http.ServeFile(w,r,"html/api/index.html")
	} else if r.URL.Path == "/api/style.css" {
		http.ServeFile(w,r,"html/api/style.css")
	} else if r.URL.Path == "/api/script.js" {
		http.ServeFile(w,r,"html/api/script.js")
	} else {
		w.Write([]byte("400 bad request"))
	}
}
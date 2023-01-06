package router

import "net/http"

func ApiManual(w http.ResponseWriter, r *http.Request) {
	http.ServeFile(w,r,"html/api.html")
}
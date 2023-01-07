package router

import "net/http"
import "fmt"

func ApiManual(w http.ResponseWriter, r *http.Request) {
	fmt.Println(r.URL.Path)
	if r.URL.Path != "/api/" {
		w.Write([]byte("400 bad request"))
		return
	}
	http.ServeFile(w,r,"html/api/index.html")
}
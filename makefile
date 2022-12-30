test:
	@echo '{"status":"ok"}' > test.txt
	@echo "Testing connection"
	@curl http://localhost:8000/
	@echo ""
	@echo "Sending test file"
	@curl -X POST -F "file=@test.txt" http://localhost:8000/geojson/
	@echo ""
	@echo "Check saved file contents"
	@curl http://localhost:8000/geojson/test.txt
	@rm -rf test.txt
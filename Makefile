release:
	npm run build
	mkdir release
	cp -r build/* release/
	pyinstaller main.py --onefile
	cp -r dist/* release/
	rm -rf build/ dist/
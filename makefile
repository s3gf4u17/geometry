run:
	docker-compose up --detach

purge:
	docker stop cnt-backend
	docker container rm cnt-backend
	docker system prune --all --force --volumes
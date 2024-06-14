runimg:
		@docker run --rm --name notes -it -p 8080:8080 -v $$(pwd):/app/ --env-file dot-env-template notes
buildimg:
		@docker build -t notes .

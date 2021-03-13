# MAKEFILE https://github.com/tstelzle/ToyotaProject
# AUTHORS: Tarek Stelzle

IMAGE-NAME := toyota_project_clicker_image
CONTAINER-NAME := toyotaProjectClicker
APP-DIR := $(PWD)/app
REPEATS := 2

build-image:
	docker build -t $(IMAGE-NAME) .

run:
	docker run -v $(APP-DIR):/run/ToyotaProject --name $(CONTAINER-NAME) --rm $(IMAGE-NAME) $(REPEATS)

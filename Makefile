.PHONY: all
all: build

.PHONY: build
build:
	$(MAKE) build-$(shell hostname)

.PHONY: build-desktop1
build-desktop1:
	./render.py prefix=Mod4

.PHONY: format
format:
	black *.py helper/src/*.py

all: build

build:
	$(MAKE) build-$(shell hostname)

build-desktop1:
	./render.py prefix=Mod4

format:
	black *.py helper/src/*.py

all: build

build:
	$(MAKE) build-$(shell hostname)

build-desktop1:
	./render.py prefix=Mod4

build-laptop2:
	./render.py prefix=Mod4

build-tagoken-desktop1:
	./render.py prefix=Mod4


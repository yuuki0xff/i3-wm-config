ifeq ($(PREFIX_KEY),)
PREFIX_KEY = Mod4
endif

.PHONY: all
all: build

.PHONY: build
build: config

config: config.tmpl render.py Makefile
	./render.py prefix=$(PREFIX_KEY)

.PHONY: format
format:
	black *.py helper/src/*.py

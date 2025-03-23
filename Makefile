ifeq ($(PREFIX_KEY),)
PREFIX_KEY = Mod4
endif

ifeq ($(WM),)
ifneq ($(shell which i3),)
WM=i3
else ifneq ($(shell which sway),)
WM=sway
else
$(error "No supported window manager found")
endif
endif

.PHONY: all
all: build

.PHONY: build
build: config

config: config.tmpl render.py Makefile
	./render.py prefix=$(PREFIX_KEY) wm=$(WM)

.PHONY: format
format:
	black *.py helper/src/*.py

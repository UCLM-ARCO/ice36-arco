# -*- mode: makefile-gmake; coding: utf-8 -*-

all:

download:
	git clone -b 3.6 https://github.com/zeroc-ice/ice.git src

.PHONY: clean
clean:
	$(RM) -f *.xz *.upload

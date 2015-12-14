# -*- mode: makefile-gmake; coding: utf-8; truncate-lines: true -*-

include ../Make.rules

DESTDIR ?= ~

all:

install: D = $(DESTDIR)
install:

	install -d $(D)/usr/lib/arm-linux-gnueabihf

	install -m 755 $(ICE_DIR)/cpp/lib/libIceStormService.so.3.6.1 $(D)/usr/lib/arm-linux-gnueabihf/
	ln -s libIceStormService.so.3.6.1 $(D)/usr/lib/arm-linux-gnueabihf/libIceStormService.so.36

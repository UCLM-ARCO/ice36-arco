# -*- mode: makefile-gmake; coding: utf-8; truncate-lines: true -*-

include ../Make.rules

DESTDIR ?= ~

all:

install: D = $(DESTDIR)
install:

	install -d $(D)/usr/lib/arm-linux-gnueabihf

	install -m 755 $(ICE_DIR)/cpp/lib/libFreeze.so.3.6.1 $(D)/usr/lib/arm-linux-gnueabihf/
	ln -s libFreeze.so.3.6.1 $(D)/usr/lib/arm-linux-gnueabihf/libFreeze.so.36
	install -m 755 $(ICE_DIR)/cpp/lib/libIceXML.so.3.6.1 $(D)/usr/lib/arm-linux-gnueabihf/
	ln -s libIceXML.so.3.6.1 $(D)/usr/lib/arm-linux-gnueabihf/libIceXML.so.36

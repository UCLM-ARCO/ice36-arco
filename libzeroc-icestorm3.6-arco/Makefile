# -*- mode: makefile-gmake; coding: utf-8; truncate-lines: true -*-

include ../Make.rules

DESTDIR ?= ~

all:

install: D = $(DESTDIR)
install:

	install -d $(D)$(LIBDIR)

	install -m 755 $(ICE_DIR)/cpp/lib/$(TRIPLET)/libIceStormService.so.3.6.1 $(D)$(LIBDIR)/
	ln -s libIceStormService.so.3.6.1 $(D)$(LIBDIR)/libIceStormService.so.36

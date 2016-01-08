# -*- mode: makefile-gmake; coding: utf-8; truncate-lines: true -*-

include ../Make.rules

DESTDIR ?= ~

all:

install: D = $(DESTDIR)
install:

	install -d $(D)$(LIBDIR)

	install -m 755 $(ICE_DIR)/cpp/lib/libFreeze.so.3.6.1 $(D)$(LIBDIR)/
	ln -s libFreeze.so.3.6.1 $(D)$(LIBDIR)/libFreeze.so.36
	install -m 755 $(ICE_DIR)/cpp/lib/libIceXML.so.3.6.1 $(D)$(LIBDIR)/
	ln -s libIceXML.so.3.6.1 $(D)$(LIBDIR)/libIceXML.so.36

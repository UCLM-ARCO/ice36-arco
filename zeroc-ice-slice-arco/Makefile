# -*- mode: makefile-gmake; coding: utf-8; truncate-lines: true -*-

include ../Make.rules

DESTDIR ?= ~

all:

install: D = $(DESTDIR)
install:

	install -d $(D)/usr/share/Ice-$(ICE_VER)/
	cp -r $(ICE_DIR)/slice $(D)/usr/share/Ice-$(ICE_VER)/

	install -d $(D)/usr/share/slice

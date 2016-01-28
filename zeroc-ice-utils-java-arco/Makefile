# -*- mode: makefile-gmake; coding: utf-8; truncate-lines: true -*-

include ../Make.rules

DESTDIR ?= ~

all:

install: D = $(DESTDIR)
install:
	install -d $(D)/usr/bin/
	install -m 755 icegridgui.sh $(D)/usr/bin/icegridgui

	install -d $(D)/usr/share/java/
	install -m 644 $(ICE_DIR)/java/lib/icegridgui.jar $(D)/usr/share/java/

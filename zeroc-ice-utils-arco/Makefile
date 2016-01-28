# -*- mode: makefile-gmake; coding: utf-8; truncate-lines: true -*-

include ../Make.rules

DESTDIR ?= ~

all:

install: D = $(DESTDIR)
install:
	install -d $(D)/usr/share/man/man1/
	install -m 644 $(ICE_DIR)/man/man1/icegridadmin.1 $(D)/usr/share/man/man1/
	install -m 644 $(ICE_DIR)/man/man1/icepatch2client.1 $(D)/usr/share/man/man1/
	install -m 644 $(ICE_DIR)/man/man1/slice2html.1 $(D)/usr/share/man/man1/
	install -m 644 $(ICE_DIR)/man/man1/icepatch2calc.1 $(D)/usr/share/man/man1/
	install -m 644 $(ICE_DIR)/man/man1/iceboxadmin.1 $(D)/usr/share/man/man1/
	install -m 644 $(ICE_DIR)/man/man1/icestormmigrate.1 $(D)/usr/share/man/man1/
	install -m 644 $(ICE_DIR)/man/man1/icestormadmin.1 $(D)/usr/share/man/man1/
	install -m 644 $(ICE_DIR)/man/man1/transformdb.1 $(D)/usr/share/man/man1/
	install -m 644 $(ICE_DIR)/man/man1/dumpdb.1 $(D)/usr/share/man/man1/

	install -d $(D)/usr/bin/
	install -m 755 $(ICE_DIR)/cpp/bin/icepatch2calc $(D)/usr/bin/
	install -m 755 $(ICE_DIR)/cpp/bin/icepatch2client $(D)/usr/bin/
	install -m 755 $(ICE_DIR)/cpp/bin/transformdb $(D)/usr/bin/
	install -m 755 $(ICE_DIR)/cpp/bin/icegridadmin $(D)/usr/bin/
	install -m 755 $(ICE_DIR)/cpp/bin/icestormmigrate $(D)/usr/bin/
	install -m 755 $(ICE_DIR)/cpp/bin/slice2html $(D)/usr/bin/
	install -m 755 $(ICE_DIR)/cpp/bin/icestormadmin $(D)/usr/bin/
	install -m 755 $(ICE_DIR)/cpp/bin/iceboxadmin $(D)/usr/bin/
	install -m 755 $(ICE_DIR)/cpp/bin/dumpdb $(D)/usr/bin/

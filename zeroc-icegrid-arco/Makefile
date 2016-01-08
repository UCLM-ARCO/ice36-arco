# -*- mode: makefile-gmake; coding: utf-8; truncate-lines: true -*-

include ../Make.rules

DESTDIR ?= ~

all:

install: D = $(DESTDIR)
install:
	install -d $(D)/var/lib/ice/icegrid/node1
	install -d $(D)/var/lib/ice/icegrid/registry

	install -d $(D)/etc/init.d

	install -m 755 debian/icegridnode.init $(D)/etc/init.d/icegridnode
	install -m 755 debian/icegridregistry.init $(D)/etc/init.d/icegridregistry

	install -m 644 debian/icegridnode.conf $(D)/etc/
	install -m 644 debian/icegridregistry.conf $(D)/etc/

	install -d $(D)/lib/systemd/system

	install -m 644 debian/icegridregistry.service $(D)/lib/systemd/system/
	install -m 644 debian/icegridnode.service $(D)/lib/systemd/system/

	install -d $(D)/usr/bin

	install -m 755 $(ICE_DIR)/cpp/bin/icegridregistry $(D)/usr/bin/
	install -m 755 $(ICE_DIR)/cpp/bin/icegridnode $(D)/usr/bin/

	install -d $(D)/usr/share/man/man1

	install -m 644 $(ICE_DIR)/man/man1/icegridnode.1 $(D)/usr/share/man/man1/
	install -m 644 $(ICE_DIR)/man/man1/icegridregistry.1 $(D)/usr/share/man/man1/

	install -d $(D)/usr/share/doc/zeroc-icegrid

	install -d $(D)/usr/share/Ice-3.6.1

	install -m 644 $(ICE_DIR)/cpp/config/icegrid-slice.3.6.ice.gz $(D)/usr/share/Ice-3.6.1/
	install -m 644 $(ICE_DIR)/cpp/config/templates.xml $(D)/usr/share/Ice-3.6.1/
	install -m 755 $(ICE_DIR)/cpp/config/upgradeicegrid36.py $(D)/usr/share/Ice-3.6.1/
	install -m 644 $(ICE_DIR)/cpp/config/icegrid-slice.3.5.ice.gz $(D)/usr/share/Ice-3.6.1/

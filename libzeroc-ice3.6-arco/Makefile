# -*- mode: makefile-gmake; coding: utf-8; truncate-lines: true -*-

include ../Make.rules

DESTDIR ?= ~

all:

install: D = $(DESTDIR)
install:

	install -d $(D)$(LIBDIR)

	install -m 755 $(ICE_DIR)/cpp/lib/$(TRIPLET)/libIce.so.3.6.1 $(D)$(LIBDIR)/
	install -m 755 $(ICE_DIR)/cpp/lib/$(TRIPLET)/libIceLocatorDiscovery.so.3.6.1 $(D)$(LIBDIR)/
	install -m 755 $(ICE_DIR)/cpp/lib/$(TRIPLET)/libIceUtil.so.3.6.1 $(D)$(LIBDIR)/
	install -m 755 $(ICE_DIR)/cpp/lib/$(TRIPLET)/libIceGrid.so.3.6.1 $(D)$(LIBDIR)/
	install -m 755 $(ICE_DIR)/cpp/lib/$(TRIPLET)/libIceDiscovery.so.3.6.1 $(D)$(LIBDIR)/
	install -m 755 $(ICE_DIR)/cpp/lib/$(TRIPLET)/libIceSSL.so.3.6.1 $(D)$(LIBDIR)/
	install -m 755 $(ICE_DIR)/cpp/lib/$(TRIPLET)/libIcePatch2.so.3.6.1 $(D)$(LIBDIR)/
	install -m 755 $(ICE_DIR)/cpp/lib/$(TRIPLET)/libIceStorm.so.3.6.1 $(D)$(LIBDIR)/
	install -m 755 $(ICE_DIR)/cpp/lib/$(TRIPLET)/libSlice.so.3.6.1 $(D)$(LIBDIR)/
	install -m 755 $(ICE_DIR)/cpp/lib/$(TRIPLET)/libGlacier2CryptPermissionsVerifier.so.3.6.1 $(D)$(LIBDIR)/
	install -m 755 $(ICE_DIR)/cpp/lib/$(TRIPLET)/libIceBox.so.3.6.1 $(D)$(LIBDIR)/
	install -m 755 $(ICE_DIR)/cpp/lib/$(TRIPLET)/libGlacier2.so.3.6.1 $(D)$(LIBDIR)/

	ln -s libIce.so.3.6.1 $(D)$(LIBDIR)/libIce.so.36
	ln -s libIceLocatorDiscovery.so.3.6.1 $(D)$(LIBDIR)/libIceLocatorDiscovery.so.36
	ln -s libIceUtil.so.3.6.1 $(D)$(LIBDIR)/libIceUtil.so.36
	ln -s libIceGrid.so.3.6.1 $(D)$(LIBDIR)/libIceGrid.so.36
	ln -s libIceDiscovery.so.3.6.1 $(D)$(LIBDIR)/libIceDiscovery.so.36
	ln -s libIceSSL.so.3.6.1 $(D)$(LIBDIR)/libIceSSL.so.36
	ln -s libIcePatch2.so.3.6.1 $(D)$(LIBDIR)/libIcePatch2.so.36
	ln -s libIceStorm.so.3.6.1 $(D)$(LIBDIR)/libIceStorm.so.36
	ln -s libSlice.so.3.6.1 $(D)$(LIBDIR)/libSlice.so.36
	ln -s libGlacier2CryptPermissionsVerifier.so.3.6.1 $(D)$(LIBDIR)/libGlacier2CryptPermissionsVerifier.so.36
	ln -s libIceBox.so.3.6.1 $(D)$(LIBDIR)/libIceBox.so.36
	ln -s libGlacier2.so.3.6.1 $(D)$(LIBDIR)/libGlacier2.so.36

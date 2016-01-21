# -*- mode: makefile-gmake; coding: utf-8; truncate-lines: true -*-

include ../Make.rules

DESTDIR ?= ~

all:

install: D = $(DESTDIR)
install:

	install -d $(D)$(LIBDIR)

	for dir in IceStorm Glacier2 IceBox Ice Slice IceGrid Freeze IceSSL IcePatch2 IceUtil; do \
	  install -d $(D)/usr/include/$$dir; \
	  cp $(ICE_DIR)/cpp/include/$$dir/*.h $(D)/usr/include/$$dir/; \
	done

	ln -s libIceDiscovery.so.36 $(D)$(LIBDIR)/libIceDiscovery.so
	ln -s libSlice.so.36 $(D)$(LIBDIR)/libSlice.so
	ln -s libIceLocatorDiscovery.so.36 $(D)$(LIBDIR)/libIceLocatorDiscovery.so
	ln -s libIceGrid.so.36 $(D)$(LIBDIR)/libIceGrid.so
	ln -s libIceBox.so.36 $(D)$(LIBDIR)/libIceBox.so
	ln -s libGlacier2CryptPermissionsVerifier.so.36 $(D)$(LIBDIR)/libGlacier2CryptPermissionsVerifier.so
	ln -s libIceSSL.so.36 $(D)$(LIBDIR)/libIceSSL.so
	ln -s libGlacier2.so.36 $(D)$(LIBDIR)/libGlacier2.so
	ln -s libIcePatch2.so.36 $(D)$(LIBDIR)/libIcePatch2.so
	ln -s libIce.so.36 $(D)$(LIBDIR)/libIce.so
	ln -s libIceUtil.so.36 $(D)$(LIBDIR)/libIceUtil.so
	ln -s libIceStorm.so.36 $(D)$(LIBDIR)/libIceStorm.so
	ln -s libFreeze.so.36 $(D)$(LIBDIR)/libFreeze.so

# -*- mode: makefile-gmake; coding: utf-8; truncate-lines: true -*-

include ../Make.rules

DESTDIR ?= ~

all:

install: D = $(DESTDIR)
install:

	install -d $(D)/usr/lib/arm-linux-gnueabihf

	install -m 755 $(ICE_DIR)/cpp/lib/libIce.so.3.6.1 $(D)/usr/lib/arm-linux-gnueabihf/
	install -m 755 $(ICE_DIR)/cpp/lib/libIceLocatorDiscovery.so.3.6.1 $(D)/usr/lib/arm-linux-gnueabihf/
	install -m 755 $(ICE_DIR)/cpp/lib/libIceUtil.so.3.6.1 $(D)/usr/lib/arm-linux-gnueabihf/
	install -m 755 $(ICE_DIR)/cpp/lib/libIceGrid.so.3.6.1 $(D)/usr/lib/arm-linux-gnueabihf/
	install -m 755 $(ICE_DIR)/cpp/lib/libIceDiscovery.so.3.6.1 $(D)/usr/lib/arm-linux-gnueabihf/
	install -m 755 $(ICE_DIR)/cpp/lib/libIceSSL.so.3.6.1 $(D)/usr/lib/arm-linux-gnueabihf/
	install -m 755 $(ICE_DIR)/cpp/lib/libIcePatch2.so.3.6.1 $(D)/usr/lib/arm-linux-gnueabihf/
	install -m 755 $(ICE_DIR)/cpp/lib/libIceStorm.so.3.6.1 $(D)/usr/lib/arm-linux-gnueabihf/
	install -m 755 $(ICE_DIR)/cpp/lib/libSlice.so.3.6.1 $(D)/usr/lib/arm-linux-gnueabihf/
	install -m 755 $(ICE_DIR)/cpp/lib/libGlacier2CryptPermissionsVerifier.so.3.6.1 $(D)/usr/lib/arm-linux-gnueabihf/
	install -m 755 $(ICE_DIR)/cpp/lib/libIceBox.so.3.6.1 $(D)/usr/lib/arm-linux-gnueabihf/
	install -m 755 $(ICE_DIR)/cpp/lib/libGlacier2.so.3.6.1 $(D)/usr/lib/arm-linux-gnueabihf/

	ln -s libIce.so.3.6.1 $(D)/usr/lib/arm-linux-gnueabihf/libIce.so.36
	ln -s libIceLocatorDiscovery.so.3.6.1 $(D)/usr/lib/arm-linux-gnueabihf/libIceLocatorDiscovery.so.36
	ln -s libIceUtil.so.3.6.1 $(D)/usr/lib/arm-linux-gnueabihf/libIceUtil.so.36
	ln -s libIceGrid.so.3.6.1 $(D)/usr/lib/arm-linux-gnueabihf/libIceGrid.so.36
	ln -s libIceDiscovery.so.3.6.1 $(D)/usr/lib/arm-linux-gnueabihf/libIceDiscovery.so.36
	ln -s libIceSSL.so.3.6.1 $(D)/usr/lib/arm-linux-gnueabihf/libIceSSL.so.36
	ln -s libIcePatch2.so.3.6.1 $(D)/usr/lib/arm-linux-gnueabihf/libIcePatch2.so.36
	ln -s libIceStorm.so.3.6.1 $(D)/usr/lib/arm-linux-gnueabihf/libIceStorm.so.36
	ln -s libSlice.so.3.6.1 $(D)/usr/lib/arm-linux-gnueabihf/libSlice.so.36
	ln -s libGlacier2CryptPermissionsVerifier.so.3.6.1 $(D)/usr/lib/arm-linux-gnueabihf/libGlacier2CryptPermissionsVerifier.so.36
	ln -s libIceBox.so.3.6.1 $(D)/usr/lib/arm-linux-gnueabihf/libIceBox.so.36
	ln -s libGlacier2.so.3.6.1 $(D)/usr/lib/arm-linux-gnueabihf/libGlacier2.so.36

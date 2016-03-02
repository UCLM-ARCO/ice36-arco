# -*- mode: makefile-gmake; coding: utf-8; truncate-lines: true -*-

include ../Make.rules

DESTDIR ?= ~

all:

install: D = $(DESTDIR)
install:

# 	install -d $(D)$(LIBDIR)
#
# 	for dir in IceStorm Glacier2 IceBox Ice Slice IceGrid Freeze IceSSL IcePatch2 IceUtil; do \
# 	  install -d $(D)/usr/include/$$dir; \
# 	  cp $(ICE_DIR)/cpp/include/$$dir/*.h $(D)/usr/include/$$dir/; \
# 	done
#
# 	ln -s libIceDiscovery.so.36 $(D)$(LIBDIR)/libIceDiscovery.so
# 	ln -s libSlice.so.36 $(D)$(LIBDIR)/libSlice.so
# 	ln -s libIceLocatorDiscovery.so.36 $(D)$(LIBDIR)/libIceLocatorDiscovery.so
# 	ln -s libIceGrid.so.36 $(D)$(LIBDIR)/libIceGrid.so
# 	ln -s libIceBox.so.36 $(D)$(LIBDIR)/libIceBox.so
# 	ln -s libGlacier2CryptPermissionsVerifier.so.36 $(D)$(LIBDIR)/libGlacier2CryptPermissionsVerifier.so
# 	ln -s libIceSSL.so.36 $(D)$(LIBDIR)/libIceSSL.so
# 	ln -s libGlacier2.so.36 $(D)$(LIBDIR)/libGlacier2.so
# 	ln -s libIcePatch2.so.36 $(D)$(LIBDIR)/libIcePatch2.so
# 	ln -s libIce.so.36 $(D)$(LIBDIR)/libIce.so
# 	ln -s libIceUtil.so.36 $(D)$(LIBDIR)/libIceUtil.so
# 	ln -s libIceStorm.so.36 $(D)$(LIBDIR)/libIceStorm.so
# 	ln -s libFreeze.so.36 $(D)$(LIBDIR)/libFreeze.so


	install -d $(D)/usr/share/java/
	install -m 644 $(ICE_DIR)/java/lib/icediscovery-3.6.1.jar $(D)/usr/share/java/
	install -m 644 $(ICE_DIR)/java/lib/icestorm-3.6.1-source.jar $(D)/usr/share/java/
	install -m 644 $(ICE_DIR)/java/lib/icegrid-3.6.1.jar $(D)/usr/share/java/
	install -m 644 $(ICE_DIR)/java/lib/icebox-3.6.1.jar $(D)/usr/share/java/
	install -m 644 $(ICE_DIR)/java/lib/icelocatordiscovery-3.6.1.jar $(D)/usr/share/java/
	install -m 644 $(ICE_DIR)/java/lib/icegrid-3.6.1-source.jar $(D)/usr/share/java/
	install -m 644 $(ICE_DIR)/java/lib/icebox-3.6.1-source.jar $(D)/usr/share/java/
	install -m 644 $(ICE_DIR)/java/lib/freeze-3.6.1.jar $(D)/usr/share/java/
	install -m 644 $(ICE_DIR)/java/lib/icestorm-3.6.1.jar $(D)/usr/share/java/
	install -m 644 $(ICE_DIR)/java/lib/ice-3.6.1-source.jar $(D)/usr/share/java/
	install -m 644 $(ICE_DIR)/java/lib/freeze-3.6.1-source.jar $(D)/usr/share/java/
	install -m 644 $(ICE_DIR)/java/lib/icediscovery-3.6.1-source.jar $(D)/usr/share/java/
	install -m 644 $(ICE_DIR)/java/lib/glacier2-3.6.1.jar $(D)/usr/share/java/
	install -m 644 $(ICE_DIR)/java/lib/ice-3.6.1.jar $(D)/usr/share/java/
	install -m 644 $(ICE_DIR)/java/lib/icepatch2-3.6.1.jar $(D)/usr/share/java/
	install -m 644 $(ICE_DIR)/java/lib/icelocatordiscovery-3.6.1-source.jar $(D)/usr/share/java/
	install -m 644 $(ICE_DIR)/java/lib/icepatch2-3.6.1-source.jar $(D)/usr/share/java/
	install -m 644 $(ICE_DIR)/java/lib/glacier2-3.6.1-source.jar $(D)/usr/share/java/

	install -d $(D)/usr/share/maven-repo/com/zeroc/freeze/3.6.1/
	install -m 644 $(ICE_DIR)/java/lib/freeze-3.6.1.pom $(D)/usr/share/maven-repo/com/zeroc/freeze/3.6.1/

	install -d $(D)/usr/share/maven-repo/com/zeroc/icestorm/3.6.1/
	install -m 644 $(ICE_DIR)/java/lib/icestorm-3.6.1.pom $(D)/usr/share/maven-repo/com/zeroc/icestorm/3.6.1/

	install -d $(D)/usr/share/maven-repo/com/zeroc/icediscovery/3.6.1/
	install -m 644 $(ICE_DIR)/java/lib/icediscovery-3.6.1.pom $(D)/usr/share/maven-repo/com/zeroc/icediscovery/3.6.1/

	install -d $(D)/usr/share/maven-repo/com/zeroc/glacier2/3.6.1/
	install -m 644 $(ICE_DIR)/java/lib/glacier2-3.6.1.pom $(D)/usr/share/maven-repo/com/zeroc/glacier2/3.6.1/

	install -d $(D)/usr/share/maven-repo/com/zeroc/icegrid/3.6.1/
	install -m 644 $(ICE_DIR)/java/lib/icegrid-3.6.1.pom $(D)/usr/share/maven-repo/com/zeroc/icegrid/3.6.1/

	install -d $(D)/usr/share/maven-repo/com/zeroc/icepatch2/3.6.1/
	install -m 644 $(ICE_DIR)/java/lib/icepatch2-3.6.1.pom $(D)/usr/share/maven-repo/com/zeroc/icepatch2/3.6.1/

	install -d $(D)/usr/share/maven-repo/com/zeroc/icelocatordiscovery/3.6.1/
	install -m 644 $(ICE_DIR)/java/lib/icelocatordiscovery-3.6.1.pom $(D)/usr/share/maven-repo/com/zeroc/icelocatordiscovery/3.6.1/

	install -d $(D)/usr/share/maven-repo/com/zeroc/icebox/3.6.1/
	install -m 644 $(ICE_DIR)/java/lib/icebox-3.6.1.pom $(D)/usr/share/maven-repo/com/zeroc/icebox/3.6.1/

	install -d $(D)/usr/share/maven-repo/com/zeroc/ice/3.6.1/
	install -m 644 $(ICE_DIR)/java/lib/ice-3.6.1.pom $(D)/usr/share/maven-repo/com/zeroc/ice/3.6.1/

	install -d $(D)/usr/bin/
	install -m 755 $(ICE_DIR)/cpp/bin/slice2freezej $(D)/usr/bin/
	install -m 755 $(ICE_DIR)/cpp/bin/slice2java $(D)/usr/bin/

	ln -s icelocatordiscovery-3.6.1.jar $(D)/usr/share/java/icelocatordiscovery.jar
	ln -s icepatch2-3.6.1.jar $(D)/usr/share/java/icepatch2.jar
	ln -s icelocatordiscovery-3.6.1-source.jar $(D)/usr/share/java/icelocatordiscovery-source.jar
	ln -s freeze-3.6.1.jar $(D)/usr/share/java/freeze.jar
	ln -s icegrid-3.6.1.jar $(D)/usr/share/java/icegrid.jar
	ln -s ice-3.6.1.jar $(D)/usr/share/java/ice.jar
	ln -s freeze-3.6.1-source.jar $(D)/usr/share/java/freeze-source.jar
	ln -s icediscovery-3.6.1-source.jar $(D)/usr/share/java/icediscovery-source.jar
	ln -s ice-3.6.1-source.jar $(D)/usr/share/java/ice-source.jar
	ln -s glacier2-3.6.1.jar $(D)/usr/share/java/glacier2.jar
	ln -s icepatch2-3.6.1-source.jar $(D)/usr/share/java/icepatch2-source.jar
	ln -s icestorm-3.6.1-source.jar $(D)/usr/share/java/icestorm-source.jar
	ln -s icediscovery-3.6.1.jar $(D)/usr/share/java/icediscovery.jar
	ln -s glacier2-3.6.1-source.jar $(D)/usr/share/java/glacier2-source.jar
	ln -s icebox-3.6.1-source.jar $(D)/usr/share/java/icebox-source.jar
	ln -s icegrid-3.6.1-source.jar $(D)/usr/share/java/icegrid-source.jar
	ln -s icestorm-3.6.1.jar $(D)/usr/share/java/icestorm.jar
	ln -s icebox-3.6.1.jar $(D)/usr/share/java/icebox.jar

	ln -s ../../../../../java/freeze-3.6.1.jar $(D)/usr/share/maven-repo/com/zeroc/freeze/3.6.1/freeze-3.6.1.jar
	ln -s ../../../../../java/freeze-3.6.1-source.jar $(D)/usr/share/maven-repo/com/zeroc/freeze/3.6.1/freeze-3.6.1-source.jar
	ln -s ../../../../../java/icestorm-3.6.1-source.jar $(D)/usr/share/maven-repo/com/zeroc/icestorm/3.6.1/icestorm-3.6.1-source.jar
	ln -s ../../../../../java/icestorm-3.6.1.jar $(D)/usr/share/maven-repo/com/zeroc/icestorm/3.6.1/icestorm-3.6.1.jar
	ln -s ../../../../../java/icediscovery-3.6.1.jar $(D)/usr/share/maven-repo/com/zeroc/icediscovery/3.6.1/icediscovery-3.6.1.jar
	ln -s ../../../../../java/icediscovery-3.6.1-source.jar $(D)/usr/share/maven-repo/com/zeroc/icediscovery/3.6.1/icediscovery-3.6.1-source.jar
	ln -s ../../../../../java/glacier2-3.6.1.jar $(D)/usr/share/maven-repo/com/zeroc/glacier2/3.6.1/glacier2-3.6.1.jar
	ln -s ../../../../../java/glacier2-3.6.1-source.jar $(D)/usr/share/maven-repo/com/zeroc/glacier2/3.6.1/glacier2-3.6.1-source.jar
	ln -s ../../../../../java/icegrid-3.6.1.jar $(D)/usr/share/maven-repo/com/zeroc/icegrid/3.6.1/icegrid-3.6.1.jar
	ln -s ../../../../../java/icegrid-3.6.1-source.jar $(D)/usr/share/maven-repo/com/zeroc/icegrid/3.6.1/icegrid-3.6.1-source.jar
	ln -s ../../../../../java/icepatch2-3.6.1.jar $(D)/usr/share/maven-repo/com/zeroc/icepatch2/3.6.1/icepatch2-3.6.1.jar
	ln -s ../../../../../java/icepatch2-3.6.1-source.jar $(D)/usr/share/maven-repo/com/zeroc/icepatch2/3.6.1/icepatch2-3.6.1-source.jar
	ln -s ../../../../../java/icelocatordiscovery-3.6.1.jar $(D)/usr/share/maven-repo/com/zeroc/icelocatordiscovery/3.6.1/icelocatordiscovery-3.6.1.jar
	ln -s ../../../../../java/icelocatordiscovery-3.6.1-source.jar $(D)/usr/share/maven-repo/com/zeroc/icelocatordiscovery/3.6.1/icelocatordiscovery-3.6.1-source.jar
	ln -s ../../../../../java/icebox-3.6.1.jar $(D)/usr/share/maven-repo/com/zeroc/icebox/3.6.1/icebox-3.6.1.jar
	ln -s ../../../../../java/icebox-3.6.1-source.jar $(D)/usr/share/maven-repo/com/zeroc/icebox/3.6.1/icebox-3.6.1-source.jar
	ln -s ../../../../../java/ice-3.6.1-source.jar $(D)/usr/share/maven-repo/com/zeroc/ice/3.6.1/ice-3.6.1-source.jar
	ln -s ../../../../../java/ice-3.6.1.jar $(D)/usr/share/maven-repo/com/zeroc/ice/3.6.1/ice-3.6.1.jar

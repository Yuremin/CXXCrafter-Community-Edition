For the 51 projects that failed to build due to missing dependencies, we searched their documentation for dependency information and compared it with the dependency issues encountered during manual builds. This allowed us to identify the missing dependency information in the project documentation.

We searched for txt or markdown files in the root directory or in the docs, build, compile, and install directories, specifically looking for files with names containing the following keywords: 

+ README
+ CONTRIBUTING
+ COMPILE
+ INSTALL
+ BUILDING

The names of the 51 projects and missing dependencies in project documentation are listed below.

| Product | Missing Dependency in Project's Documentation |
| --- | --- |
| gcc |  |
| codon |  |
| clang | llvm-17 |
| gdb | gmp |
| raylib | XInput |
| OpenRCT2 | flac, vorbisfile |
| minetest | OpenGL |
| guetzli |  |
| openalpr |  |
| openpose |  |
| aseprite | Xinput |
| mozjepg |  |
| gpt4all | qt6, OpenGL |
| caffee |  |
| paddle | python, numpy, protobuf, patchelf |
| rethinkdb | OpenSSL |
| rocksdb |  |
| sqlitebrowser |  |
| arangodb | nghttp2, boehm-gc, snappy |
| FFmpeg | nasm |
| libvpx | nasm |
| openh264 |  |
| vireo |  |
| theora |  |
| blender | libx11-dev, libegl-dev, libdbus-1-dev, linux-libc-dev |
| shotcut | mlt++-7, XKB, WrapVulkanHeaders, |
| libde265 |  |
| soloud | ALSA |
| MuseScore | OpenGL, WrapVulkanHeaders, ALSA |
| wav2letter | Flashlight |
| audioFlux | setuptools |
| treefrog-framework |  |
| pistache |  |
| cpprestsdk |  |
| Crow | boost |
| drogon | jsoncpp |
| lwan |  |
| NanoGUI | xi, cursor |
| RmlUi |  |
| xtd | asoundlib |
| flameshot |  |
| Qv2ray | protobuf, grpc, qt5, qt5svg |
| polybar |  |
| DearPyGui | x11, xinerama, xcursor, opengl, libffi-dev |
| jucipp | libtinfo |
| color_coded |  |
| Codelite |  |
| rtags |  |
| qt-creator | XKB, WrapVulkanHeaders, libdbus-1 |
| cquery | libtinfo5 |
| Irony-mode | libtinfo5 |


| **Project Name** | **Inclusion of Test files** | **Test Commands** | **Test Success** | **Version Check** | **Build Output Consistency** |
| :---: | --- | --- | --- | --- | --- |
| GCC | No | | | | Yes |
| 8cc | Yes | make test | Yes | | Yes |
| mold | Yes | make test | Yes | | Yes |
| clang | Yes | cmake -G Ninja -DLLVM_ENABLE_PROJECTS=clang -DCMAKE_BUILD_TYPE=Release ../llvm | Yes | | Yes |
| llvm-project | Yes | cmake -G Ninja -DLLVM_ENABLE_PROJECTS=clang -DCMAKE_BUILD_TYPE=Release ../llvm | Yes | | Yes |
| GDB | Yes | ./testbed.out | Yes | | Yes |
| Linux | No | | | | Yes |
| ReactOS | No | | | | Yes |
| Godot | No | | | Yes | Yes |
| Gameplay | No | | | | Yes |
| Raylib | No | | | | Yes |
| Doom | No | | | | Yes |
| EnTT | No | | | | Yes |
| Stockfish | Yes | ./tests/instrumented.sh   ./tests/perft.sh   ./tests/signature.sh   ./tests/reprosearch.sh | No | Yes | Yes |
| OpenRCT2 | No | | |  | Yes |
| MineTest | No | | | Yes | Yes |
| Guetzli | No | | | Yes | Yes |
| OpenALPR | No | | | | Yes |
| Aseprite | Yes | cmake -G Ninja -DCMAKE_BUILD_TYPE=RelWithDebInfo -DLAF_BACKEND=skia -DSKIA_DIR=$HOME/deps/skia -DSKIA_LIBRARY_DIR=$HOME/deps/skia/out/Release-x64 -DSKIA_LIBRARY=$HOME/deps/skia/out/Release-x64/libskia.a -DCMAKE_CXX_COMPILER=clang++ -DCMAKE_C_COMPILER=clang -DCMAKE_CXX_FLAGS="-stdlib=libc++" -DCMAKE_EXE_LINKER_FLAGS="-stdlib=libc++" -DCMAKE_SHARED_LINKER_FLAGS="-stdlib=libc++" .. | Yes | | Yes |
| Tesseract | No | | | Yes | Yes |
| MozJpeg | Yes | make test | Yes | | Yes |
| Libfacedetection | No | | | | Yes |
| Libjpeg-turbo | Yes | ./tjunittest | Yes | | Yes |
| Libjxl | Yes | ./bash_test.sh | Yes | | Yes |
| Simdjson | No | | | | Yes |
| XGBoost | No | | | | Yes |
| OpenCV | Yes | make test | Yes | | Yes |
| Llama.cpp | No | | | Yes | Yes |
| Caffe | Yes | make test | Yes | | Yes |
| Paddle | No | | | Yes | Yes |
| mxnet | No | | | Yes | Yes |
| rethinkdb | No | | | Yes | Yes |
| mongo | No | | | | |
| leveldb | Yes | make test | Yes | | Yes |
| rocksdb | Yes | make check | Yes | | Yes |
| sqlitebrowser | Yes | | Yes |  | Yes |
| kvrocks | No | | | Yes | Yes |
| FFmpeg | No | | | Yes | Yes |
| libvpx | Yes | ./test_libvpx | Yes | | Yes |
| openh264 | No | | | | Yes |
| vireo | No | | | | Yes |
| theora | No | | | | Yes |
| x265 | No | | | Yes | Yes |
| libde265 | No | | | | Yes |
| rnnoise | No | | | | Yes |
| soloud | No | | | | Yes |
| aubio | Yes | | Yes | | Yes |
| libsndfile | Yes | ./CMakeBuild/Command_test | Yes | | Yes |
| libsoundio | Yes | ./build/unit_tests | No | | Yes |
| audioFlux | No | | | | Yes |
| treefrog-framework | No | | | Yes | Yes |
| civetweb | No | | | Yes | Yes |
| pistache | No | | | | Yes |
| cpprestsdk | No | | | | Yes |
| Crow | Yes | ./build/tests | Yes | | Yes |
| Drogon | No | | | Yes | Yes |
| facil.io | No | | | | Yes |
| lwan | Yes | | Yes | | Yes |
| Oatpp | Yes | ./build/test/oatppAllTests | Yes | | Yes |
| userver | No | | | | Yes |
| NanoGUI | Yes | ./build/example1 | Yes | | Yes |
| RmlUi | No | | | | Yes |
| elements | No | | | | Yes |
| libui | No | | | | Yes |
| flameshot | No | | | Yes | Yes |
| polybar | No | | | Yes | Yes |
| DearPyGui | No | | | | Yes |
| webui | No | | | | Yes |
| Geany | No | | | Yes | Yes |
| Code::Blocks | No | | |  | Yes |
| jucipp | No | | | | Yes |
| color_coded | No | | | | Yes |
| rtags | No | | | | Yes |
| cquery | Yes | ./build/cquery --test | Yes | | Yes |
| Irony-mode | No | | | Yes | Yes |



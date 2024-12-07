# how to install googletest

## Method 1

```bash
apt-get install libgtest-dev
```

## Method 2

need `cmake`
```bash
apt-get install cmake
brew install cmake
```

install `googletest`
```bash
git clone https://github.com/google/googletest gtest
cd gtest
mkdir build
cd build
cmake ../ \
  -DCMAKE_CXX_FLAGS=-std=c++17 \
  -DCMAKE_CXX_STANDARD=17 \
  -DCMAKE_C_COMPILER="/usr/bin/clang" \
  -DCMAKE_CXX_COMPILER="/usr/bin/clang++" \
  -DCMAKE_INSTALL_PREFIX=$(realpath "$(pwd)/../../")
make
make install
cd ../../
rm -rf gtest
```

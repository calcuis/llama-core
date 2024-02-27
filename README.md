### llama-core
[<img src="https://raw.githubusercontent.com/calcuis/llama-core/master/lime.gif" width="128" height="128">](https://github.com/calcuis/llama-core)
[![Static Badge](https://img.shields.io/badge/core-0.1.8-lime?logo=github)](https://github.com/calcuis/llama-core/releases)

This is a solo llama connector also; being able to work independently.

#### install via (pip/pip3):
```
pip install llama-core
```
#### run it by (python/python3):
```
python -m llama_core
```

[<img src="https://raw.githubusercontent.com/calcuis/llama-core/master/demo.png" width="235" height="95">](https://github.com/calcuis/llama-core/blob/main/demo.png)

Prompt to user interface selection menu above; while chosen, GGUF file(s) in the current directory will be searched and detected (if any) as below.

[<img src="https://raw.githubusercontent.com/calcuis/chatgpt-model-selector/master/demo.gif" width="350" height="280">](https://github.com/calcuis/chatgpt-model-selector/blob/main/demo.gif)
[<img src="https://raw.githubusercontent.com/calcuis/chatgpt-model-selector/master/demo1.gif" width="350" height="280">](https://github.com/calcuis/chatgpt-model-selector/blob/main/demo1.gif)

#### include interface selector to your code by adding:
```
from llama_core import menu
```
#### include gguf reader to your code by adding:
```
from llama_core import reader
```
#### include gguf writer to your code by adding:
```
from llama_core import writer
```

#### remark(s)
Other functions are same as llama-cpp-python; for CUDA(GPU, Nvida) and Metal(M1/M2, Apple) supported settings, please specify `CMAKE_ARGS` following Abetlen's repo below; if you want to install it by source file (under releases), you should opt to do it by .tar.gz file (then build your machine-customized installable package) rather than .whl (wheel; a pre-built binary package) with an appropriate cmake tag(s).
#### references
repo [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)
[llama.cpp](https://github.com/ggerganov/llama.cpp)
page [gguf.us](https://gguf.us)
#### build from llama_core-(version).tar.gz (examples below are for CPU)
According to the latest note inside vs code, msys64 is recommended by Microsoft; or you can opt w64devkit or etc. as source of your gcc and g++ compilers.
#### for windows user(s):
```
$env:CMAKE_GENERATOR = "MinGW Makefiles"
$env:CMAKE_ARGS = "-DCMAKE_C_COMPILER=C:/msys64/mingw64/bin/gcc.exe -DCMAKE_CXX_COMPILER=C:/msys64/mingw64/bin/g++.exe"
pip install llama_core-(version).tar.gz
```
In mac, xcode command line tools are recommended by Apple for dealing all coding related issue(s); or you can bypass it for your own good/preference.
#### for mac user(s):
```
pip3 install llama_core-(version).tar.gz
```
Make sure your gcc and g++ are >=11; you can check it by: gcc --version and g++ --version; other setting(s) include: cmake>=3.21, etc.; however, if you opt to install it by the pre-built wheel (.whl) file then you don't need to worry about that.

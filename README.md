### llama-core
[<img src="https://raw.githubusercontent.com/calcuis/gguf-connector/master/gguf.gif" width="128" height="128">](https://github.com/calcuis/llama-core)
[![Static Badge](https://img.shields.io/badge/core-0.0.3-blue?logo=github)](https://github.com/calcuis/llama-core/releases)

This is a solo llama connector; being able to work independently.

#### install via (pip/pip3):
```
pip install llama-core
```
#### run it by (python/python3):
```
python -m llama_core
```
[<img src="https://raw.githubusercontent.com/calcuis/chatgpt-model-selector/master/demo.gif" width="350" height="280">](https://github.com/calcuis/chatgpt-model-selector/blob/main/demo.gif)
[<img src="https://raw.githubusercontent.com/calcuis/chatgpt-model-selector/master/demo1.gif" width="350" height="280">](https://github.com/calcuis/chatgpt-model-selector/blob/main/demo1.gif)

Other functions are same as llama-cpp-python; for CUDA(GPU, Nvida) and Metal(M1/M2, Apple) supported settings, please specify `CMAKE_ARGS` following Abetlen's repo below; if you want to install it by source file (under releases), you should opt to do it by .tar.gz file (then build your machine customized installable package) rather than .whl (wheel; a pre-built binary package) with an appropriate cmake tag(s).
### References
[llama-cpp-python](https://github.com/abetlen/llama-cpp-python)
[llama.cpp](https://github.com/ggerganov/llama.cpp)

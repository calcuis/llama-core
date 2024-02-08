cmake_minimum_required(VERSION 3.21)
project(llama_core)

option(LLAMA_BUILD "Build llama.cpp shared library and install alongside python package" ON)
option(LLAVA_BUILD "Build llava shared library and install alongside python package" ON)

if (LLAMA_BUILD)
    set(BUILD_SHARED_LIBS "On")

    if (APPLE AND NOT CMAKE_SYSTEM_PROCESSOR MATCHES "arm64")
        set(LLAMA_AVX "Off" CACHE BOOL "llama: enable AVX" FORCE)
        set(LLAMA_AVX2 "Off" CACHE BOOL "llama: enable AVX2" FORCE)
        set(LLAMA_FMA "Off" CACHE BOOL "llama: enable FMA" FORCE)
        set(LLAMA_F16C "Off" CACHE BOOL "llama: enable F16C" FORCE)
    endif()
    add_subdirectory(vendor/llama.cpp)
    install(
        TARGETS llama 
        LIBRARY DESTINATION ${SKBUILD_PLATLIB_DIR}/llama_core
        RUNTIME DESTINATION ${SKBUILD_PLATLIB_DIR}/llama_core
        ARCHIVE DESTINATION ${SKBUILD_PLATLIB_DIR}/llama_core
        FRAMEWORK DESTINATION ${SKBUILD_PLATLIB_DIR}/llama_core
        RESOURCE DESTINATION ${SKBUILD_PLATLIB_DIR}/llama_core
    )
    install(
        TARGETS llama 
        LIBRARY DESTINATION ${CMAKE_CURRENT_SOURCE_DIR}/llama_core
        RUNTIME DESTINATION ${CMAKE_CURRENT_SOURCE_DIR}/llama_core
        ARCHIVE DESTINATION ${CMAKE_CURRENT_SOURCE_DIR}/llama_core
        FRAMEWORK DESTINATION ${CMAKE_CURRENT_SOURCE_DIR}/llama_core
        RESOURCE DESTINATION ${CMAKE_CURRENT_SOURCE_DIR}/llama_core
    )
    install(
        FILES $<TARGET_RUNTIME_DLLS:llama>
        DESTINATION ${SKBUILD_PLATLIB_DIR}/llama_core
    )
    install(
        FILES $<TARGET_RUNTIME_DLLS:llama>
        DESTINATION ${CMAKE_CURRENT_SOURCE_DIR}/llama_core
    )

    if (LLAVA_BUILD)
        add_subdirectory(vendor/llama.cpp/examples/llava)
        set_target_properties(llava_shared PROPERTIES OUTPUT_NAME "llava")
        if (WIN32)
            set_target_properties(llava_shared PROPERTIES CUDA_ARCHITECTURES OFF)
        endif()
        install(
            TARGETS llava_shared
            LIBRARY DESTINATION ${SKBUILD_PLATLIB_DIR}/llama_core
            RUNTIME DESTINATION ${SKBUILD_PLATLIB_DIR}/llama_core
            ARCHIVE DESTINATION ${SKBUILD_PLATLIB_DIR}/llama_core
            FRAMEWORK DESTINATION ${SKBUILD_PLATLIB_DIR}/llama_core
            RESOURCE DESTINATION ${SKBUILD_PLATLIB_DIR}/llama_core
        )
        install(
            TARGETS llava_shared
            LIBRARY DESTINATION ${CMAKE_CURRENT_SOURCE_DIR}/llama_core
            RUNTIME DESTINATION ${CMAKE_CURRENT_SOURCE_DIR}/llama_core
            ARCHIVE DESTINATION ${CMAKE_CURRENT_SOURCE_DIR}/llama_core
            FRAMEWORK DESTINATION ${CMAKE_CURRENT_SOURCE_DIR}/llama_core
            RESOURCE DESTINATION ${CMAKE_CURRENT_SOURCE_DIR}/llama_core
        )
    endif()
endif()

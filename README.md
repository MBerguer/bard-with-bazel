# Minimal Project built on top of Bazel

## Description:
This project showcases the minimum configuration required to set up a Python project with [Bazel](https://bazel.build/), the last build system you'll ever need. This repo serves as a practical demonstration to introduce participants to the basic structure and concepts of using Bazel, and it could be easily changed to any other programming language using the power of rules.

## How to?
0. (if you don't have it already) Install bazelisk
    1. `npm install -g @bazel/bazelisk` (there are more ways to install it if you don't have npm, see: https://github.com/bazelbuild/bazelisk )
    2. `bazel` see if it was installed correctly
1. Get the token from bard API, and create a `.env` with the token you just got.
    1. Follow instructions here: https://github.com/dsdanielpark/Bard-API
    2. `cp .env.example .env`
2. Update requirements_lock.txt
    1. `bazel run //:requirements.update` this step is needed if more dependencies are added.
3. Build:
    - 3.1 Build: `bazel build //src/...`
    - 3.2 Run: `bazel test --action_env=$(cat .env | xargs) tests/...`

4. Enjoy!


## Overview
Here is a short desciption of how the the repo is structured.

### Files
```
.
├── BUILD.bazel
├── README.md
├── requirements_lock.txt
├── requirements.txt
├── src
│   ├── bard_module.py
│   ├── bard_module_test.py
│   └── BUILD.bazel
└── WORKSPACE
```

The project includes a simple Python application that consists of two source files: `bard_module.py` and `bard_module_test.py`. 
The bard_module.py file contains the entry point of the application, while `bard_module_test.py` provides a sample module.

The project utilizes a requirements.txt file to declare its Python dependencies. These dependencies will be managed and resolved by Bazel during the build process.

The `WORKSPACE` file defines the external dependencies and repositories, while the `BUILD.bazel` file specifies the build directives for our Python application.

### Notes:

- This is the minimal configuration of this Python project with Bazel. It provides a solid foundation for understanding the key concepts of Bazel's build system and its integration with Python projects, and it was created for demo purpouses. Take in consideration that there are more improvemets we can do if we plan to run this in a production environment.

- This description can be further expanded and customized to match the specific details and objectives of your workshop.

# CXXCrafter
A tool designed to automatically build C/C++ projects.

## Overview

CXXCrafter is an automated C/C++ project build tool that leverages the implicit knowledge storage and semantic understanding capabilities of LLMs. Utilizing a RAG framework, it extracts build information from project repositories, generates, and iteratively modifies Dockerfiles to build the project, until a successful build is achieved.



## Features
- **Multi-Build System Compatibility:** Supports a wide array of mainstream C/C++ build systems and scripts, including Make, CMake, Autotools, Ninja, Meson, Bazel, Xmake, Build2, Vcpkg, Python, and Shell.
- **Automated Build Entry Detection:** Intelligently identifies the build entry file without manual intervention.
- **Customizable Build Solutions:** User can specify particular build demands, and CXXCrafter will tailor build plans to meet those needs.
- **High Success Rate:** Tested on popular GitHub projects, with an overall success rate exceeding 70%, it can effectively overcome numerous challenges encountered in manual builds.
- **High Throughput Efficiency:**  Capable of handling a large number of projects in parallel.

## Installation Guide
1. Clone the repository:
```
git clone https://github.com/Yuremin/CXXCrafter.git
```

2. CXXCrafter is written using Python 3.9. Make sure to install all dependencies of the right version:

```
python==3.9
openai==1.25.0
json5==0.9.14
beautifulsoup4==0.0.1
bs4==0.0.1
GitPython==3.1.40
lxml==4.9.3
requests==2.31.0
certifi==2023.11.17
charset-normalizer==3.3.2
gitdb==4.0.11
idna==3.4
smmap==5.0.1
soupsieve==2.5
urllib3==2.1.0
docker==7.1.0
qdrant-client==1.11.1
tiktoken==0.7.0
```

## Usage Example
1. Collect the paths of projects to be built, and save them in a text file, for instance:
```
projects/gcc
projects/8cc
projects/codon
projects/mold
projects/clang
projects/llvm-project
projects/emacs-gdb
...
```
2. Run the CXXCrafter script with the text file as an argument:
```
cd CXXCrafter
python3 src/run.py --project_path_list=path_to_your_project_list.txt
```
3. Dockerfiles which have implemented a succesful build, will be saved to directory `./build_solution_base`. For build history and logs, refer to `./dockerfile_playground` and `./logs` directories, respectively. 








# CXXCrafter: A tool designed to automatically build C/C++ projects.

CXXCrafter is an automated C/C++ project build tool that leverages the implicit knowledge storage and semantic understanding capabilities of LLMs. Utilizing a RAG framework, it extracts build information from project repositories, generates, and iteratively modifies Dockerfiles to build the project, until a successful build is achieved.

- **Multi-Build System Compatibility:** Supports a wide array of mainstream C/C++ build systems and scripts, including Make, CMake, Autotools, Ninja, Meson, Bazel, Xmake, Build2, Vcpkg, Python, and Shell.
- **Automated Build Entry Detection:** Intelligently identifies the build entry file without manual intervention.
- **Customizable Build Solutions:** User can specify particular build demands, and CXXCrafter will tailor build plans to meet those needs.
- **High Success Rate:** Tested on popular GitHub projects, with an overall success rate exceeding 70%, it can effectively overcome numerous challenges encountered in manual builds.
- **High Throughput Efficiency:**  Capable of handling a large number of projects in parallel.

## News
+ **[2025.04.01]** CXXCrafter has been accepted by FSE(ESEC) 2025. 🎉🎉🎉

## Quick Start
1. Clone the repository:
```
git clone https://github.com/Yuremin/CXXCrafter.git
```

2. CXXCrafter is written using 大于等于Python 3.9. 

可以选择使用`uv`等虚拟环境

```
pip install .
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

## Cite

```bibtex
@inproceedings{Yu2025CXXCrafter,
  title={CXXCrafter: An LLM-Based Agent for Automated C/C++ Open Source Software Building},
  author={Zhengmin Yu, Yuan Zhang, Ming Wen, Yinan Nie, Wenhui Zhang and Min Yang},
  journal={Proceedings of the ACM on Software Engineering},
  volume={1},
  number={FSE},
  year={2025}
}
```



## Licenses

[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)

This project adheres to the [MIT License](https://lbesson.mit-license.org/).

[![CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](http://creativecommons.org/licenses/by-nc-sa/4.0/)

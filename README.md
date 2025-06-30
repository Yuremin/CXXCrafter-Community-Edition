# **CXXCrafter: An Automated C/C++ Project Build Tool**

**CXXCrafter** is an LLM Agent that automates C/C++ builds by generating and refining Dockerfiles.

### Highlights

- Supports mainstream C/C++ build systems
- Auto-detects build entry
- 70%+ success on real projects
- High parallel throughput

## News

- **[2025.04.01]** CXXCrafter has been accepted to **FSE (ESEC) 2025**! 🎉🎉🎉

## Quick Start

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Yuremin/CXXCrafter.git
   ```

2. **Environment setup:**  
   CXXCrafter requires **Python 3.9 or higher**.  
   You can optionally use a virtual environment manager like [`uv`](https://github.com/astral-sh/uv):

   ```bash
   pip install .
   ```

## Usage Example

1. **Prepare the project list:**  
   Save the absolute or relative paths of the C/C++ projects you wish to build into a text file, for example:

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

2. **Run CXXCrafter:**

   ```bash
   cd CXXCrafter
   python3 src/run.py --project_path_list=path_to_your_project_list.txt
   ```

3. **Check results:**  

   - Successfully generated Dockerfiles will be stored in `./build_solution_base`.
   - Build logs and history can be found in `./dockerfile_playground` and `./logs`, respectively.

## Citation

If you use **CXXCrafter** in your work, please cite:

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

## License

This project is released under the [MIT License](https://lbesson.mit-license.org/).

[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)  
[![CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](http://creativecommons.org/licenses/by-nc-sa/4.0/)
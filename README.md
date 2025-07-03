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
   git clone https://github.com/Yuremin/CXXCrafter-Community-Edition.git
   ```

2. **Environment setup:**  
    CXXCrafter requires **Python 3.9 or higher**. You can optionally use a virtual environment manager like [`uv`](https://github.com/astral-sh/uv).
   - First, install CXXCrafter as a Python package:
     ```bash
     cd CXXCrafter-Community-Edition 
     pip install .
     ```
   - Then, start `Docker daemon` on your machine.

## Usage Example

### Build a single project
```bash
python -m cxxcrafter --repo /path/to/your/project
```

### Build project batch 

- **Prepare the project list:**  
 Save the absolute or relative paths of the C/C++ projects you wish to build into a text file, for example:

  ```
  /path/to/project1
  /path/to/project2
  /path/to/project3
  /path/to/project4
  ...
  ```
- **Run CXXCrafter:**
  ```bash
  python -m cxxcrafter --repo-list /path/to/your/repo/list/file
  ```

### Check results

   - Successfully generated Dockerfiles will be stored in `~/.cxxcrafter/build_solution_base`.
   - Build logs and history can be found in `~/.cxxcrafter/dockerfile_playground` and `~/.cxxcrafter/logs`, respectively.

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
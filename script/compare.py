import os

file1 = 'data/top100/repo_link.txt'
file2 = 'data/oss-fuzz/oss-fuzz-projects.txt'

with open(file1, 'r') as f:
    content1s = f.readlines()

with open(file2, 'r') as f:
    content2s = f.readlines()

new_content2s = []
for content2 in content2s:
    if content2 in content1s:
        continue
    else:
        new_content2s.append(content2)

with open('data/oss-fuzz/new_repo_link.txt', 'w') as f:
    for i in new_content2s:
        f.write(i)
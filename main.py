import os

files = os.listdir("../_posts")
for file in files:
    with open(path := os.path.join("../_posts/", file), "r", encoding="UTF-8") as f:
        if "报告者" in f.read():
            os.remove(path)
            print(file)

import os
import shutil

from textnode import TextNode, TextType

def main():
    copy_static()

def copy_static():
    if not os.path.exists("public/"):
        os.mkdir("public/")

    shutil.rmtree("public/", ignore_errors=True)
    shutil.copytree("static/", "public/")

if __name__ == "__main__":
    main()

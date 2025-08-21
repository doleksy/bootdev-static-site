import os
import shutil

from generate import generate_page
from textnode import TextNode, TextType

def main():
    copy_static()

def copy_static():
    if not os.path.exists("public/"):
        os.mkdir("public/")

    shutil.rmtree("public/", ignore_errors=True)
    shutil.copytree("static/", "public/")

    from_path = "./content/index.md"
    template_path = "./template.html"
    dest_path = "./public/index.html"
    generate_page(from_path, template_path, dest_path)

if __name__ == "__main__":
    main()

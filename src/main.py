import os
import shutil

from generate import generate_page, generate_pages_recursive
from textnode import TextNode, TextType

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    if not os.path.exists(dir_path_public):
        os.mkdir(dir_path_public)

    shutil.rmtree(dir_path_public, ignore_errors=True)
    shutil.copytree(dir_path_static, dir_path_public)

    generate_pages_recursive(dir_path_content, template_path, dir_path_public)

if __name__ == "__main__":
    main()

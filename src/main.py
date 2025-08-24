import os
import shutil
import sys

from generate import generate_page, generate_pages_recursive
from textnode import TextNode, TextType

dir_path_static = "./static"
#dir_path_public = "./public"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"
default_basepath = "/"

def main():
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    
    if not os.path.exists(dir_path_public):
        os.mkdir(dir_path_public)

    shutil.rmtree(dir_path_public, ignore_errors=True)
    shutil.copytree(dir_path_static, dir_path_public)

    generate_pages_recursive(basepath, dir_path_content, template_path, dir_path_public)

if __name__ == "__main__":
    main()

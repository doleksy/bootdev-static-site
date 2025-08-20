import os

from markdown import markdown_to_html_node, extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    markdown = ""
    with open(from_path) as f_markdown:
        markdown = f_markdown.read()
        print(markdown)

    template = ""
    with open(template_path) as f_template:
        template = f_template.read()
        print(template)

    nodes = markdown_to_html_node(markdown)
    print(nodes)
    content = nodes.to_html()
    print(content)

    title = extract_title(markdown)
    print(title)

    full_page = template.replace("{{ Title }}", title).replace("{{ Content }}", content)
    print(full_page)

    dirname = os.path.dirname(dest_path)
    os.makedirs(dirname, exist_ok=True)

    with open(dest_path, mode='w') as f_dest:
        f_dest.write(full_page)

def test_generate_page():
    from_path = "content/index.md"
    template_path = "./template.html"
    dest_path = "./dolek.html"
    generate_page(from_path, template_path, dest_path)

if __name__ == "__main__":
    test_generate_page()

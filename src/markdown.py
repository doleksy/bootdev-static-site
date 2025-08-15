from blocks import BlockType, block_to_block_type, markdown_to_blocks
from node_to_node import text_node_to_html_node
from parentnode import ParentNode
from textnode import TextNode, TextType
from text_to_textnode import text_to_textnodes




def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)

    html_nodes = []
    for block in blocks:
        print(f"block: {block}")
        block_type = block_to_block_type(block)
        print(f"Block type: {block_type.value}")

        if block_type == BlockType.PARAGRAPH:
            child_nodes = text_to_children(block)

            parent = ParentNode("p", block)
            html_nodes.append(parent)

    return ParentNode("div", html_nodes)

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    print(f"Text nodes: {text_nodes}")
    return [text_node_to_html_node(node) for node in text_nodes]

def test_paragraphs():
    md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

    node = markdown_to_html_node(md)
    print(node)
    html = node.to_html()
    print(html)

def test_codeblock():
    md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

    node = markdown_to_html_node(md)
    print(node)
    html = node.to_html()
    print(html)

if __name__ == "__main__":
    test_paragraphs()
    #test_codeblock()
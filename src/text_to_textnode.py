from split import split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import TextNode, TextType


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.TEXT)
    nodes = split_nodes_delimiter(nodes, "_", TextType.TEXT)
    nodes = split_nodes_delimiter(nodes, "`", TextType.TEXT)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes


def test():
    text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    nodes = text_to_textnodes(text)
    print(nodes)
#   [
#       TextNode("This is ", TextType.TEXT),
#       TextNode("text", TextType.BOLD),
#       TextNode(" with an ", TextType.TEXT),
#       TextNode("italic", TextType.ITALIC),
#       TextNode(" word and a ", TextType.TEXT),
#       TextNode("code block", TextType.CODE),
#       TextNode(" and an ", TextType.TEXT),
#       TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
#       TextNode(" and a ", TextType.TEXT),
#       TextNode("link", TextType.LINK, "https://boot.dev"),
#   ]

if __name__ == "__main__":
    test()
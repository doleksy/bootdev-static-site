from leafnode import LeafNode
from textnode import TextNode, TextType

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    if text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})

def test():
    node = TextNode("This is a text node", TextType.TEXT)
    html_node = text_node_to_html_node(node)
    print(html_node.to_html())

    node = TextNode("This is a bold node", TextType.BOLD)
    html_node = text_node_to_html_node(node)
    print(html_node.to_html())

    node = TextNode("This is an italic node", TextType.ITALIC)
    html_node = text_node_to_html_node(node)
    print(html_node.to_html())

    node = TextNode("This is a code node", TextType.CODE)
    html_node = text_node_to_html_node(node)
    print(html_node.to_html())

    node = TextNode("This is a link node", TextType.LINK)
    html_node = text_node_to_html_node(node)
    print(html_node.to_html())

    node = TextNode("This is an image node", TextType.IMAGE)
    html_node = text_node_to_html_node(node)
    print(html_node.to_html())

if __name__ == "__main__":
    test()    
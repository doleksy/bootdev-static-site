from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    delim_type = None
    if delimiter == "**":
        delim_type = TextType.BOLD
    elif delimiter == "_":
        delim_type = TextType.ITALIC
    elif delimiter == "`":
        delim_type = TextType.CODE

    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            text_split = node.text.split(delimiter)
            if len(text_split) % 2 == 0:
                raise ValueError("invalid markdown, formatted section not closed")
            
            for idx in range(0, len(text_split)):
                if text_split[idx] == "":
                    continue

                if idx % 2 == 0:
                    new_nodes.append(TextNode(text_split[idx], TextType.TEXT))
                else:
                    new_nodes.append(TextNode(text_split[idx], delim_type))
    #print(new_nodes)
    return new_nodes


def test():
    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    node_b = TextNode("bold word", TextType.BOLD)
    new_nodes = split_nodes_delimiter([node, node_b], "`", TextType.CODE)
    print(new_nodes)

    node = TextNode("**bold** and _italic_", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    print(new_nodes)

if __name__ == "__main__":
    test()

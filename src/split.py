from extractmarkdown import extract_markdown_images, extract_markdown_links
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

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        original_text = node.text

        image_matches = extract_markdown_images(original_text)
        if image_matches:
            for match in image_matches:
                sections = original_text.split(f"![{match[0]}]({match[1]})", 1)

                if len(sections) != 2:
                    raise ValueError("invalid markdown, image section not closed")

                if sections[0] != "":
                    new_nodes.append(TextNode(sections[0], TextType.TEXT))
                new_nodes.append(TextNode(match[0], TextType.IMAGE, match[1]))

                original_text = sections[1]

            if original_text != "":
                new_nodes.append(TextNode(original_text, TextType.TEXT))
        else:
            new_nodes.append(node)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        original_text = node.text

        link_matches = extract_markdown_links(original_text)
        if link_matches:
            for match in link_matches:
                sections = original_text.split(f"[{match[0]}]({match[1]})", 1)

                if len(sections) != 2:
                    raise ValueError("invalid markdown, link section not closed")

                if sections[0] != "":
                    new_nodes.append(TextNode(sections[0], TextType.TEXT))
                new_nodes.append(TextNode(match[0], TextType.LINK, match[1]))

                original_text = sections[1]
            
            if original_text != "":
                new_nodes.append(TextNode(original_text, TextType.TEXT))

        else:
            new_nodes.append(node)
    return new_nodes

def test_split_nodes_delimeter():
    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    node_b = TextNode("bold word", TextType.BOLD)
    new_nodes = split_nodes_delimiter([node, node_b], "`", TextType.CODE)
    print(new_nodes)

    node = TextNode("**bold** and _italic_", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    print(new_nodes)

def test_split_nodes_image():
    node = TextNode(
        "This is text with an image ![boot image](https://www.boot.dev/boot.png) and ![youtube logo](https://www.youtube.com/logo.jpg)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_image([node])
    print(new_nodes)
    # [
    #     TextNode("This is text with a link ", TextType.TEXT),
    #     TextNode("boot image", TextType.IMAGE, "https://www.boot.dev/boot.png"),
    #     TextNode(" and ", TextType.TEXT),
    #     TextNode(
    #         "youtube logo", TextType.IMAGE, "https://www.youtube.com/logo.jpg"
    #     ),
    # ]    

def test_split_nodes_link():
    node = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_link([node])
    print(new_nodes)
    # [
    #     TextNode("This is text with a link ", TextType.TEXT),
    #     TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
    #     TextNode(" and ", TextType.TEXT),
    #     TextNode(
    #         "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
    #     ),
    # ]    

if __name__ == "__main__":
    #test_split_nodes_delimeter()
    test_split_nodes_image()
    #test_split_nodes_link()

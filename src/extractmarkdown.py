import re


image_match = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
# Takes raw markdown text and returns a list of tuples.
# Each tuple should contain the alt text and the URL of any markdown images.
def extract_markdown_images(text):
    matches = re.findall(image_match, text)
    return matches

link_match = r"\[([^\[\]]*)\]\(([^\(\)]*)\)"
# Takes raw markdown text and returns a list of tuples.
# Each tuple should contain the alt text and the URL of any markdown images.
def extract_markdown_links(text):
    matches = re.findall(link_match, text)
    return matches

def test():
    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    print(extract_markdown_images(text))
    # [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]

    text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    print(extract_markdown_links(text))
    # [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]

    test  = "There are no images or links here."
    print(extract_markdown_images(text))
    # []

if __name__ == "__main__":
    test()

from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    def __eq__(self, o):
        return (self.text == o.text) and (self.text_type == o.text_type) and (self.url == o.url)
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def test():
    node = TextNode("This is a text node", TextType.BOLD, "http://www.example.com")
    print(node)

if __name__ == "__main__":
    test()

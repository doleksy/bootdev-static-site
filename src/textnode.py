from enum import Enum

class TextType(Enum):
    PLAIN = "plain"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    def __eq__(o):
        return (self.text == o.text) and (self.text_type == o.text_type) and (self.url == o.url)
    def __repr__():
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def test():
    print("hello test")

if __name__ == "__main__":
    test()

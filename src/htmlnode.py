class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        result = ""
        if self.props:
            for key,value in self.props.items():
                result += f' {key}="{value}"'
        return result

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props_to_html()})"
    
def test():
    props = {
        "href": "https://www.google.com",
        "target": "_blank",
    }
    node = HTMLNode("<p>", "blah", "child", props)
    print(node)

if __name__ == "__main__":
    test()

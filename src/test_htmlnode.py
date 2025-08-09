import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_default(self):
        node = HTMLNode()
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_props(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode(props=props)
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, None)
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_default(self):
        child1 = HTMLNode("<p>", "child1")
        child2 = HTMLNode("<p>", "child2")
        node = HTMLNode(children=[child1, child2])
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, [child1, child2])
        self.assertEqual(node.props, None)

if __name__ == "__main__":
    unittest.main()

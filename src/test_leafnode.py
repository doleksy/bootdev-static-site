import unittest

from leafnode import LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_none_causes_value_error(self):
        with self.assertRaises(ValueError):
            LeafNode(None, None).to_html()

    def test_leaf_to_html_raw_text(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_p_outputs_html(self):
        html = LeafNode("p", "This is a paragraph of text.").to_html()
        self.assertEqual(html, "<p>This is a paragraph of text.</p>")

    def test_a_with_props_outputs_html(self):
        html = LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
        self.assertEqual(html, '<a href="https://www.google.com">Click me!</a>')

if __name__ == "__main__":
    unittest.main()

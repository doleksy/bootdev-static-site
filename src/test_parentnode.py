import unittest

from leafnode import LeafNode
from parentnode import ParentNode


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_with_many_children(self):
        parent_node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            parent_node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_to_html_with_many_children_and_props(self):
        parent_node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text", {"href": "https://www.bold.com"}),
                LeafNode(None, "Normal text", {"href": "https://www.shouldnt_see.com"}),
                LeafNode("i", "italic text", {"href": "https://www.italic.com"}),
                LeafNode(None, "Normal text", {"href": "https://www.shouldnt_see.com"}),
            ],
        )
        self.assertEqual(
            parent_node.to_html(),
            '<p><b href="https://www.bold.com">Bold text</b>Normal text<i href="https://www.italic.com">italic text</i>Normal text</p>',
        )

if __name__ == "__main__":
    unittest.main()

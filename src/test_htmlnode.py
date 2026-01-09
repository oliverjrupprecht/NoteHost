import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = HTMLNode()
        node2 = HTMLNode("bob")
        self.assertNotEqual(node, node2)

    def test_none_url(self):
        node = HTMLNode(props={"dummy":"data", "zim":"zom", "baz":"bosh"})
        self.assertEqual(node.props_to_html(), "dummy=\"data\" zim=\"zom\" baz=\"bosh\"")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")

if __name__ == "__main__":
    unittest.main()

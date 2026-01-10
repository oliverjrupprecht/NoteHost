import unittest

from textnode import TextNode, TextType, text_node_to_html_node

from split_nodes_delimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):

    def test_code(self):
        nodes = split_nodes_delimiter([TextNode("This is text with a `code block` in the middle", TextType.TEXT)], "`", TextType.CODE)
        self.assertEqual(nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" in the middle", TextType.TEXT),
        ])

    def test_italic(self):
        nodes = split_nodes_delimiter([TextNode("This is text with a _italic block_ in the middle", TextType.TEXT)], "_", TextType.ITALIC)
        self.assertEqual(nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("italic block", TextType.ITALIC),
            TextNode(" in the middle", TextType.TEXT),
        ])


    def test_bold(self):
        nodes = split_nodes_delimiter([TextNode("This is text with a **bold block** in the middle", TextType.TEXT)], "**", TextType.BOLD)
        self.assertEqual(nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold block", TextType.BOLD),
            TextNode(" in the middle", TextType.TEXT),
        ])

    def test_list(self):
        nodes = split_nodes_delimiter([TextNode("This is text with a `code block` in the middle", TextType.TEXT)], "`", TextType.CODE)
        nodes.extend(
        split_nodes_delimiter([TextNode("This is text with a _italic block_ in the middle", TextType.TEXT)], "_", TextType.ITALIC))
        nodes.extend(
        split_nodes_delimiter([TextNode("This is text with a **bold block** in the middle", TextType.TEXT)], "**", TextType.BOLD))

        output = [ 
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" in the middle", TextType.TEXT),
            
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("italic block", TextType.ITALIC),
            TextNode(" in the middle", TextType.TEXT),

            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold block", TextType.BOLD),
            TextNode(" in the middle", TextType.TEXT),
                 ]
        self.assertEqual(nodes, output)

if __name__ == "__main__":
    unittest.main()

import unittest

from textnode import TextNode, TextType, text_node_to_html_node

from split_nodes_delimiter import split_nodes_delimiter

from split_nodes_image import split_nodes_image

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

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

if __name__ == "__main__":
    unittest.main()

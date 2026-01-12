from textnode import TextNode, TextType

from split_nodes_delimiter import split_nodes_delimiter
from split_nodes_link import split_nodes_link
from split_nodes_image import split_nodes_image

def text_to_textnodes(text):
    tn = TextNode(text, TextType.TEXT)
    return split_nodes_image(
            split_nodes_link(
                split_nodes_delimiter(
                    split_nodes_delimiter(
                        split_nodes_delimiter([tn], "**", TextType.BOLD), "`", TextType.CODE), "_", TextType.ITALIC)))


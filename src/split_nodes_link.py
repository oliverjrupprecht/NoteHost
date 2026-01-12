from textnode import TextType, TextNode
import re

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        for split in re.split(r"(\[.*?\]\(.*?\))", node.text):
            match = re.findall(r"\[(.*?)\]\((.*?)\)", split)
            
            if match != []:
                new_nodes.append(TextNode(match[0][0], TextType.LINK, match[0][1]))
            else:
                new_nodes.append(TextNode(split, TextType.TEXT))

    return new_nodes



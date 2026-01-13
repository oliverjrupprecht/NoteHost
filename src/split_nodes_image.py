from textnode import TextType, TextNode 
import re

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            for split in re.split(r"(\!\[.*?\]\(.*?\))", node.text):
                match = re.findall(r"\!\[(.*?)\]\((.*?)\)", split)
                
                if match != []:
                    new_nodes.append(TextNode(match[0][0], TextType.IMAGE, match[0][1]))
                elif split == "":
                    continue
                else:
                    new_nodes.append(TextNode(split, TextType.TEXT))

        else:
            new_nodes.append(node)

    return new_nodes



from textnode import TextType, TextNode
import re

def split_nodes_delimiter_old(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT: #if the node is not txt type we dont need too parse data from it
            new_nodes.append(node)
            continue

        if len(node.text) < 2:
            new_nodes.append(node)
            continue

        p = 0
        foundDelim = False 
        for i in range(len(node.text)): 
            shield = i + len(delimiter)

            if shield == len(node.text) - 1 and not foundDelim:
                new_nodes.append(TextNode(node.text[p:len(node.text)], TextType.TEXT))
                break

            if shield == len(node.text) - 1 and foundDelim:
                print(node.text)
                raise Exception("no closing delimiter on input text")

            if node.text[i:shield] == delimiter:
                if foundDelim:
                    new_nodes.append(TextNode(node.text[p:i], text_type))
                else:
                    new_nodes.append(TextNode(node.text[p:i], TextType.TEXT))

                foundDelim = not foundDelim 
                i = i + len(delimiter)
                p = i
                continue

    return new_nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
            
        # Split by the literal delimiter
        parts = node.text.split(delimiter)
        
        # Markdown delimiters must come in pairs
        if len(parts) % 2 == 0:
            raise ValueError("Invalid Markdown: Delimiter not closed")
            
        for i in range(len(parts)):
            if parts[i] == "":
                continue
            if i % 2 == 0:
                # Even index: Text outside delimiters
                new_nodes.append(TextNode(parts[i], TextType.TEXT))
            else:
                # Odd index: Text inside delimiters
                new_nodes.append(TextNode(parts[i], text_type))
                
    return new_nodes


def split_nodes_delimiter_other(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT: #if the node is not txt type we dont need too parse data from it
            new_nodes.append(node)
            continue
        
        p = 0
        foundDelim = False 
        for i in range(len(node.text)): 
            shield = i + len(delimiter)

            if shield == len(node.text) - 1 and not foundDelim:
                new_nodes.append(TextNode(node.text[p:len(node.text)], TextType.TEXT))
                break

            if shield == len(node.text) - 1 and foundDelim:
                raise Exception("no closing delimiter on input text")

            if node.text[i:shield] == delimiter:
                if foundDelim:
                    new_nodes.append(TextNode(node.text[p:i], text_type))
                else:
                    new_nodes.append(TextNode(node.text[p:i], TextType.TEXT))

                foundDelim = not foundDelim 
                i = i + len(delimiter)
                p = i
                continue

    return new_nodes

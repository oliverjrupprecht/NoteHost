from blocktype import BlockType
from block_to_blocktype import block_to_blocktype
from htmlnode import HTMLNode, ParentNode
from text_to_textnodes import text_to_textnodes
from textnode import TextType, text_node_to_html_node, LeafNode 

def markdown_to_html_node(markdown):
    # breaks raw text into blocks labeled by their type
    blocks = [(stripped, block_to_blocktype(stripped)) for block in markdown.split("\n\n") if (stripped := block.strip())]
     
    div_children = []
    for block in blocks:
        match block[1]:
            case BlockType.PARAGRAPH: 
                div_children.append(
                    ParentNode("p", text_to_children(block[0]) ))

            case BlockType.HEADING1:
                div_children.append(ParentNode("h1", text_to_children(block[0]) ))
                
            case BlockType.HEADING2:
                div_children.append(ParentNode("h2", text_to_children(block[0]) ))
                
            case BlockType.HEADING3:
                div_children.append(ParentNode("h3", text_to_children(block[0]) ))
                
            case BlockType.HEADING4:
                div_children.append(ParentNode("h4", text_to_children(block[0]) ))
                
            case BlockType.HEADING5:
                div_children.append(ParentNode("h5", text_to_children(block[0]) ))
                
            case BlockType.HEADING6:
                div_children.append(ParentNode("h6", text_to_children(block[0]) ))
                
            case BlockType.CODE:
                div_children.append(
                    ParentNode("pre", 
                               [LeafNode("code", value=block[0][4:-4])])
                )
                
            case BlockType.QUOTE:
                div_children.append(ParentNode("blockquote", text_to_children(block[0])))
                
            case BlockType.UNORDERED_LIST:
                div_children.append(ParentNode("ul", [ParentNode("li", text_to_children(line[2:])) for line in block[0].split("\n")]))
                
            case BlockType.ORDERED_LIST:
                div_children.append(ParentNode("ol", [ParentNode("li", text_to_children(line[3:])) for line in block[0].split("\n")]))

    return ParentNode("div", div_children)
    
def text_to_children(text) -> list[HTMLNode] :
    textnodes = text_to_textnodes(text)
    return [text_node_to_html_node(tn) for tn in textnodes]

def extract_title(markdown : str):
    for line in markdown.split("\n"):
        if line.startswith("# "):
            return line

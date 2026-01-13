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

            case BlockType.HEADING:
                div_children.append(ParentNode("h1", text_to_children(block[0]) ))
                
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


md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

another para with a link [blub](pub)
"""


cd = """
```
This is text that _should_ remainthe **same** even with inline stuff
```

hello another paragraph here 

> quotes 
> here

- and a list
- hik
- more
- bullet points

1. ne
2. number two
3. number three
"""

#othernode = (markdown_to_html_node(md))
#codenode = markdown_to_html_node(cd)
#cut = codenode.to_html()

#out = othernode.to_html()


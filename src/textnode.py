from enum import Enum

class TextType(Enum):
    PLAIN_TEXT = "plain"
    ITALIC_TEXT = "italic"
    CODE_TEXT = "code"
    LINK_TEXT = "link"
    IMAGE_TEXT = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        if not isinstance(text_type, TextType):
            raise TypeError(f"Error: {text_type} must be an instance of TextType")
        self.text_type = text_type
        self.url = url
            
    def __eq__(self, other : object): 
        if not isinstance(other, TextNode):
            return False


        rt = (
                self.text == other.text and 
                self.text_type == other.text_type and 
                self.url == other.url
                )

        return rt

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

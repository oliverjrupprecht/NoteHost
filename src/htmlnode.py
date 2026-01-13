class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None ):
        self.tag = tag # str representing HTML node name
        self.value = value # str representing text inside the node
        self.children = children # [] of child nodes
        self.props = props # dict representing attributes of the tag

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props_to_html()})"

    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False

        return (self.tag == other.tag 
                and self.value == other.value
                and self.children == other.children
                and self.props == other.props)

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        "returns ther properties of the node in HTML"
        if self.props is None:
            return ""

        out = ""
        keys = list(self.props.keys())
        for i in range(len(keys)):
            if i == len(keys) - 1:
                out += f"{keys[i]}=\"{self.props[keys[i]]}\""
            else:
                out += f"{keys[i]}=\"{self.props[keys[i]]}\" "

        return out
            
class LeafNode(HTMLNode):
    def __init__(self, tag : str, value : str, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError
        
        if self.tag is None:
            return self.value

        return f"<{self.tag}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError
        
        if self.children is None:
            raise ValueError("Error: Parent Node must have children")

        if not self.props:
            out = f"<{self.tag}>"
            for child in self.children:
                html = child.to_html()
                if html:
                    out += html

        else:
            out = f"<{self.tag} {self.props_to_html()}>"
            for child in self.children:
                html = child.to_html()
                if html:
                    out += html 

        return out + f"</{self.tag}>"

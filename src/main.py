import textnode as tn

from textnode import (TextNode, TextType)

def main():
    node = TextNode("beep boop", TextType.PLAIN_TEXT, "website")
    print(node)

main()

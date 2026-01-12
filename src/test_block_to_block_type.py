import unittest

from  block_to_blocktype import block_to_blocktype
from blocktype import BlockType

class TestSplitNodesDelimiter(unittest.TestCase):

    def test_blocks_to_headings(self):
        notheading = (block_to_blocktype("# this is not a heading\nhello"))
        heading = (block_to_blocktype("## this is a heading"))
        self.assertEqual(heading, BlockType.HEADING)
        self.assertNotEqual(notheading, BlockType.HEADING)


    def test_blocks_to_code(self):
        notcode = (block_to_blocktype("``` this is not a code block ```"))
        code = (block_to_blocktype("```\n this is a code block\n```"))
        self.assertEqual(code, BlockType.CODE)
        self.assertNotEqual(notcode, BlockType.CODE)

    def test_blocks_to_quote(self):
        quote = (block_to_blocktype("> this is a quote block\n> quotey mc quote face"))
        notquote = (block_to_blocktype(" > this is not a quote block\n quotey mc quote face"))
        self.assertEqual(quote, BlockType.QUOTE)
        self.assertNotEqual(notquote, BlockType.QUOTE)

    def test_blocks_to_ulist(self):
        ulist = (block_to_blocktype("- this is a unordered list block\n- blocky mc bloock face"))
        notulist = (block_to_blocktype("- this isnt a unordered list block\n > blocky mc bloock face"))
        self.assertEqual(ulist, BlockType.UNORDERED_LIST)
        self.assertNotEqual(notulist, BlockType.UNORDERED_LIST)

    def test_blocks_to_olist(self):
        olist = (block_to_blocktype("1. this is an ordered list block\n2. ordered mc ordered face\n3. just a third line brother"))
        notolist = (block_to_blocktype("1 this isnt an ordered list block\n2. ordered mc ordered face\n3. just a third line brother"))
        self.assertEqual(olist, BlockType.ORDERED_LIST)
        self.assertNotEqual(notolist, BlockType.ORDERED_LIST)

if __name__ == "__main__":
    unittest.main()
 

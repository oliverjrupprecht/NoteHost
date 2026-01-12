from blocktype import BlockType
import re


def block_to_blocktype(blk : str):
    
    heading_m = re.fullmatch(r"^#{1,6} .*", blk) # headings should only be one line
    if heading_m is not None:
        return BlockType.HEADING

    code_block_m = re.fullmatch(r"^```\n.*\n```$", blk) # code blocks should start and end with three backticks on a seperate line
    if code_block_m is not None:
        return BlockType.CODE

    lines = [line.strip() for line in blk.split("\n")]

    quote_complement = re.compile(r"^> .*")
    quote_block = [quote_complement.fullmatch(line) for line in lines]
    if all(quote_block): return BlockType.QUOTE


    ulist_complement = re.compile(r"^- .*")
    ulist_block = [ulist_complement.fullmatch(line) for line in lines]
    if all(ulist_block): return BlockType.UNORDERED_LIST

    # cannot pre complile for efficiency because regex is different for every line
    olist_block = [re.fullmatch(rf"^{i+1}\. .*", lines[i]) for i in range(len(lines))]
    if all(olist_block): return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH


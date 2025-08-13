from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def test_markdown_to_blocks():
    markdown =  """
# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item
    """
    blocks = markdown_to_blocks(markdown)
    print(blocks)

def test_block_to_block_type():
    type = block_to_block_type("# This is a heading")
    print(type.value)

    type = block_to_block_type("- This is an unordered list")
    print(type.value)

    type = block_to_block_type("3. This is an ordered list")
    print(type.value)

    type = block_to_block_type("```This is code.```")
    print(type.value)

    type = block_to_block_type("> This is a quote list")
    print(type.value)

    type = block_to_block_type("This is a normal paragraph")
    print(type.value)


if __name__ == "__main__":
    #test_markdown_to_blocks()
    test_block_to_block_type()
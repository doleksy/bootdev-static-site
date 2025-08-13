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
    if block.startswith("#"):
        return BlockType.HEADING
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    elif block.startswith(">"):
        return BlockType.QUOTE
    elif block.startswith("-"):
        return BlockType.UNORDERED_LIST
    elif block[0].isdigit() and block[1] == ".":
        return BlockType.ORDERED_LIST
    else:
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
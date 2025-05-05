from markdown_parser import SemanticMarkdownParser
from pathlib import Path
import json
from token_encoder.encode import get_token_length


if __name__ == "__main__":
    parser = SemanticMarkdownParser()
    input_text = Path("opt3001.md").read_text(encoding="utf-8")

    # Parse to tree
    root = parser.parse_markdown_to_tree(input_text)

    # Process tree into chunks
    chunks = parser.get_semantic_chunks(root, max_tokens=500)

    # Print resulting chunks
    with open("output.txt", "w") as file:
        for i, chunk in enumerate(chunks, 1):
            file.write(f"\nChunk {i}:\n")
            file.write("-" * 80 + "\n")
            file.write(chunk + "\n")
            file.write("-" * 80 + "\n")
            file.write(f"Token length: {get_token_length(chunk)}\n")

    print("Output saved to output.txt")

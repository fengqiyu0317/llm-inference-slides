#!/usr/bin/env python3
"""构建脚本：将三个 part 的 slide HTML 合并为单文件 index.html"""

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SLIDES_DIR = os.path.join(SCRIPT_DIR, "slides")
OUTPUT = os.path.join(SCRIPT_DIR, "index.html")

PARTS = [
    "part1-inference-basics.html",
    "part2-optimization.html",
    "part3-scaling.html",
]


def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def build():
    css = read_file(os.path.join(SLIDES_DIR, "shared-style.css"))

    sections = []
    for part in PARTS:
        path = os.path.join(SLIDES_DIR, part)
        if not os.path.exists(path):
            print(f"Warning: {part} not found, skipping")
            continue
        sections.append(read_file(path))

    slide_content = "\n".join(sections)

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>大模型推理 & Inference-Time Scaling</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/reveal.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/theme/white.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<style>
{css}
</style>
</head>
<body>
<div class="reveal">
<div class="slides">
{slide_content}
</div>
</div>
<script src="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/reveal.js"></script>
<script src="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/plugin/notes/notes.js"></script>
<script src="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/plugin/math/math.js"></script>
<script>
Reveal.initialize({{
    hash: true,
    slideNumber: true,
    width: 1280,
    height: 720,
    margin: 0.04,
    plugins: [RevealNotes, RevealMath.KaTeX],
    katex: {{
        local: '',
    }},
}});
</script>
</body>
</html>"""

    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write(html)

    total = slide_content.count("<section")
    print(f"Built {OUTPUT} with {total} slides from {len(sections)} parts")


if __name__ == "__main__":
    build()

# 大模型推理 & Inference-Time Scaling 课件项目

## 项目概述

- **课程**: 《大语言模型》，面向中高年级本科生
- **主题**: 大模型推理 & Inference-Time Scaling
- **时长**: 45 分钟
- **讲者**: 3 人，各 ~15 分钟
- **要求**: 内容严谨，涉及数学本质；三部分分割自然不突兀

## 内容结构

### Part 1: 大模型推理基础（Speaker A, ~15 min, Slide 1-9）
Attention 铺垫 → 自回归生成 → KV Cache → Prefill vs Decode → Roofline 分析 → 延迟指标

### Part 2: 推理优化技术（Speaker B, ~15 min, Slide 10-16）
量化 → 推测解码（思想 + 正确性证明 + 加速分析） → 系统级优化（Continuous Batching, PagedAttention）

### Part 3: Inference-Time Scaling（Speaker C, ~15 min, Slide 17-25）
CoT → 自一致性/多数投票 → Best-of-N + 奖励模型 → 树搜索 + PRM → 前沿模型（o1, DeepSeek R1）→ 总结

### 叙事弧线
```
Part 1: "推理为什么昂贵？" → 机制与瓶颈
Part 2: "如何让推理更快？" → 优化技术
Part 3: "如果故意花更多计算呢？" → Inference-Time Scaling
```

## 技术栈

- **课件格式**: reveal.js HTML slides
- **数学公式**: KaTeX
- **构建**: `python3 build.py` → 合并为 `index.html`
- **文件结构**:
  - `slides/part1-inference-basics.html` — Part 1 源文件
  - `slides/part2-optimization.html` — Part 2 源文件
  - `slides/part3-scaling.html` — Part 3 源文件
  - `slides/shared-style.css` — 共享样式
  - `build.py` — 构建脚本
  - `assets/` — 图表素材

## 构建与预览

```bash
python3 build.py        # 合并生成 index.html
# 浏览器打开 index.html 即可预览
# index.html#/N 跳转到第 N 页（0-based）
```

## 关键参考文献

1. Vaswani et al. (2017) — Attention Is All You Need
2. Kaplan et al. (2020) — Scaling Laws for Neural Language Models
3. Frantar et al. (2023) — GPTQ
4. Leviathan et al. (2023) — Speculative Decoding
5. Kwon et al. (2023) — PagedAttention / vLLM
6. Wei et al. (2022) — Chain-of-Thought Prompting
7. Wang et al. (2023) — Self-Consistency
8. Lightman et al. (2023) — Let's Verify Step by Step (PRM vs ORM)
9. Snell et al. (2024) — Scaling LLM Test-Time Compute Optimally
10. DeepSeek-AI (2025) — DeepSeek-R1 (GRPO, RLVR)

## 注意事项

- 修改 slide 或 CSS 后必须运行 `python3 build.py` 才能在 index.html 中生效
- 每页 slide 应包含演讲者备注 `<aside class="notes">`
- **此文件需随项目变动同步更新**

# Hexo MD 构建器（hexo-md-builder）

一个 Trae IDE Skill，专为 Hexo 博客的 Markdown 文章构建与美化而生。

## 功能速览

| 功能 | 说明 |
|------|------|
| **Word → MD** | 将 Word 文档转为 Hexo 格式 Markdown，自动生成 frontmatter |
| **MD 翻新** | 翻新旧 MD 的排版格式（自动创建备份，不覆盖原文） |
| **标题智能识别** | 即使 Word 中未使用标准标题样式，也能推断层级结构 |
| **Note 块排版** | 使用 Butterfly/NexT 的 note 标签美化文章层次 |
| **SweetAlert 弹窗** | 为术语、世界观词条添加交互式解释弹窗 |
| **文末附表** | 自动附加内容总结、情节速览、操作速查等概括性附录 |
| **HTML 预览** | 可选生成带交互动画的微缩 HTML 预览页面 |
| **语法验证** | 使用 `hexo clean && hexo g` 自动校验生成结果 |
| **中文排版规范** | 自动处理中英文空格、全角标点、专有名词大小写 |

## 使用场景

- 将 Word 写的文章转为 Hexo 博客的 Markdown 文件
- 翻新旧文章的排版，添加 note 块、弹窗、附表
- 为世界观创作类文章添加术语弹窗解释
- 为教程类文章生成操作速查表和 FAQ

## 文件结构

```
hexo-md-builder/
├── SKILL.md                          # Skill 主文件
└── references/
    ├── hexo-syntax-guide.md          # Hexo 标签语法参考
    ├── sweetalert-usage.md           # SweetAlert 弹窗使用指南
    ├── formatting-examples.md        # 排版美化示例集
    ├── html-preview-template.md      # HTML 预览页面制作指南
    └── word-to-md-guide.md           # Word 转 MD 深度指南
```

## 安装

将整个 `hexo-md-builder/` 文件夹放入 Trae IDE 的 `.trae/skills/` 目录下即可。

```
.trae/skills/hexo-md-builder/
```

## 要求

- Hexo 博客（Butterfly 或 NexT 主题以获得最佳 note 块效果）
- 使用 SweetAlert 弹窗功能需要主题已引入 sweetalert 和 jQuery

# HTML 预览页面制作指南

当用户需要快速、形象、生动地了解MD文档的关键内容时，可以制作微缩的纯HTML文件。

## 设计原则

1. **单文件自包含**：所有CSS/JS内联，不依赖外部资源
2. **主题贴合内容**：根据文章主题选择合适的配色和视觉风格
3. **关键内容提取**：提取核心章节标题和要点，而非全文复制
4. **交互驱动**：提供点击交互、展开/收起等操作
5. **动画增强**：使用CSS动画提升视觉表现力

## 配色方案参考

### 深空科技风
适合科幻、世界观设定、未来主题文章

```css
:root {
    --bg-deep: #020b18;
    --bg-panel: rgba(5, 14, 36, 0.94);
    --bg-card: rgba(8, 20, 44, 0.82);
    --accent: #1a9fb5;
    --accent-glow: #28bcd4;
    --accent-dim: #095e75;
    --text-primary: #d4e6f4;
    --text-secondary: #6e98b8;
    --text-dim: #3a6080;
    --border: rgba(61, 192, 216, 0.15);
    --border-bright: rgba(61, 192, 216, 0.45);
}
```

### 暖色人文风
适合文学、散文、回忆录类文章

```css
:root {
    --bg-deep: #1a0f08;
    --bg-panel: rgba(30, 15, 10, 0.94);
    --accent: #c9a050;
    --accent-glow: #e6b860;
    --text-primary: #f0e0c0;
    --text-secondary: #b89870;
    --border: rgba(200, 160, 80, 0.2);
}
```

### 自然清新风
适合自然、游记、生活类文章

```css
:root {
    --bg-deep: #0a1a0a;
    --bg-panel: rgba(15, 30, 15, 0.94);
    --accent: #4ad8b0;
    --accent-glow: #6ef0c0;
    --text-primary: #d0f0d0;
    --text-secondary: #80b080;
    --border: rgba(74, 216, 176, 0.2);
}
```

## 常用动画

### 垂直扫描线
```css
@keyframes scanVertical {
    0% { top: -2px; opacity: 0; }
    4% { opacity: 0.65; }
    92% { opacity: 0.65; }
    97% { opacity: 0; }
    100% { top: calc(100% + 2px); opacity: 0; }
}
```

### 脉冲点
```css
@keyframes pulseDot {
    0%, 100% { transform: translate(-50%, -50%) scale(0.5); opacity: 0.35; }
    50% { transform: translate(-50%, -50%) scale(1.5); opacity: 1; }
}
```

### 光标闪烁
```css
@keyframes cursorBlink {
    0%, 100% { opacity: 1; }
    50% { opacity: 0; }
}
```

### 淡入上浮
```css
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}
```

## 交互组件

### 卡片点击展开/收起
```javascript
document.querySelectorAll('.card').forEach(card => {
    card.addEventListener('click', () => {
        card.classList.toggle('expanded');
    });
});
```

### 星空背景（Canvas）
```javascript
const canvas = document.getElementById('bg-canvas');
const ctx = canvas.getContext('2d');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const stars = Array.from({length: 200}, () => ({
    x: Math.random() * canvas.width,
    y: Math.random() * canvas.height,
    r: Math.random() * 2 + 0.5,
    a: Math.random()
}));

function drawStars() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    stars.forEach(s => {
        ctx.beginPath();
        ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(200,220,255,${0.3 + s.a * 0.7})`;
        ctx.fill();
    });
    requestAnimationFrame(drawStars);
}
drawStars();
```

### 扫描线HUD边框
```html
<div class="hud-corner tl"></div>
<div class="hud-corner tr"></div>
<div class="hud-corner bl"></div>
<div class="hud-corner br"></div>
```

```css
.hud-corner {
    position: absolute; width: 28px; height: 28px;
    border-color: rgba(61,192,216,0.35); border-style: solid;
}
.hud-corner.tl { top: 16px; left: 16px; border-width: 1px 0 0 1px; }
.hud-corner.tr { top: 16px; right: 16px; border-width: 1px 1px 0 0; }
.hud-corner.bl { bottom: 16px; left: 16px; border-width: 0 0 1px 1px; }
.hud-corner.br { bottom: 16px; right: 16px; border-width: 0 1px 1px 0; }
```

## 页面结构模板

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>页面标题</title>
    <style>
        /* 全局样式 */
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { 
            font-family: "Microsoft YaHei", sans-serif;
            background: var(--bg-deep); color: var(--text-primary);
            overflow: hidden; height: 100vh;
        }
        /* Canvas背景 */
        #bg-canvas { position: fixed; top: 0; left: 0; z-index: 0; }
        /* 主容器 */
        #app { position: relative; z-index: 1; display: flex; height: 100%; }
        /* 内容区 */
        #main { flex: 1; display: flex; flex-direction: column; padding: 40px; }
    </style>
</head>
<body>
    <canvas id="bg-canvas"></canvas>
    <div id="app">
        <div id="main">
            <!-- 内容卡片 -->
        </div>
    </div>
    <script>
        // 交互逻辑
    </script>
</body>
</html>
```

## 彩蛋设计建议

1. **隐藏点击区域**：在页面不太显眼的位置放置一个小图标或文字，点击后触发特殊动画或信息
2. **键盘快捷键**：监听特定的键盘组合键触发彩蛋
3. **连续点击**：对某个元素连续点击多次触发隐藏效果
4. **Konami Code**：经典的 ↑↑↓↓←→←→BA 触发

```javascript
// 示例：隐藏文字彩蛋
const secret = document.getElementById('secret-easter-egg');
secret.addEventListener('click', () => {
    // 触发特殊动画
    document.body.classList.add('easter-egg-active');
    setTimeout(() => document.body.classList.remove('easter-egg-active'), 3000);
});
```

## 保存位置

HTML预览文件保存至根目录下的 `output/` 文件夹中，文件名格式建议为 `<文章名>_preview.html`。

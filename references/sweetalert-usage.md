# SweetAlert 弹窗使用指南

SweetAlert是一个美观的弹窗库，可用于在Hexo博客文章中创建交互式弹窗，解释世界观术语、自定义词条或需要用户确认的内容。

## 前置条件

SweetAlert依赖jQuery和sweetalert库。需要在Hexo主题中引入：

**Butterfly主题**：在 `inject` 的 `bottom` 处加入：
```html
<script src="https://unpkg.com/sweetalert/dist/sweetalert.min.js"></script>
```

**NexT主题**：修改 `_layout.njk`，在 `<body>` 标签后加入：
```html
<script src="https://unpkg.com/sweetalert/dist/sweetalert.min.js"></script>
```

## 点击式弹窗模板

在文章任意位置放入按钮：

```html
<button id="btn-<唯一ID>" class="btn-beautify button--animated" title="<鼠标悬停提示>">🎯 点我了解：<术语名称></button>
```

在按钮所在文章的末尾（或按钮之后）放入弹窗脚本：

```html
<script>
(function wait() {
  if (typeof $ === 'undefined' || typeof swal === 'undefined') {
    setTimeout(wait, 200);
    return;
  }
  document.getElementById('btn-<唯一ID>').addEventListener('click', function () {
    swal({
      title: "<弹窗标题>",
      text: "<弹窗正文，用于解释术语或词条的详细含义>",
      icon: "info",
      button: "知道了",
    });
  });
})();
</script>
```

### 参数说明

| 参数 | 说明 | 示例值 |
|------|------|--------|
| `<唯一ID>` | 按钮唯一标识符，与按钮id对应 | `term-huoshen` |
| `<术语名称>` | 按钮上显示的文字 | `火神契约` |
| `<鼠标悬停提示>` | title属性，鼠标悬停时显示 | `点击了解契约的含义` |
| `<弹窗标题>` | 弹窗顶部标题 | `火神契约` |
| `<弹窗正文>` | 弹窗正文内容 | `所谓"契约"，乃是以"平等"的关系来交换能力或利益...` |

### icon 类型

| icon值 | 图标样式 | 适用场景 |
|--------|----------|----------|
| `"info"` | 蓝色信息图标 | 一般术语解释、词条说明 |
| `"success"` | 绿色勾选图标 | 正面概念、成功案例 |
| `"warning"` | 黄色警告图标 | 需要注意的概念、风险提示 |
| `"error"` | 红色错误图标 | 危险概念、需要警惕的内容 |

### 按钮样式

| class | 说明 |
|-------|------|
| `btn-beautify` | 美化按钮样式 |
| `button--animated` | 添加动画效果 |
| `btn btn-primary btn-lg m-3` | Bootstrap风格按钮 |

## 自动弹窗模板（页面加载时弹出）

适用于重要通知、阅读须知等场景：

```html
<script>
if (sessionStorage.getItem("isPopupWindow") != "1") {
    swal({
      title: "TITLE",
      text: "text",
      icon: "success",
      button: "OK",
    });
    sessionStorage.setItem("isPopupWindow", "1");
}
</script>
```

使用 `sessionStorage` 确保每个会话只弹窗一次。

## 完整示例

以下是一个完整的使用示例，为文章中的"文明库"术语添加解释弹窗：

```html
<button 
  id="btn-wenmingku" 
  class="btn-beautify button--animated" 
  title="点击了解文明库的含义"
>📚 点我了解：文明库</button>

<script>
(function wait() {
  if (typeof $ === 'undefined' || typeof swal === 'undefined') {
    setTimeout(wait, 200);
    return;
  }
  document.getElementById('btn-wenmingku').addEventListener('click', function () {
    swal({
      title: "文明库",
      text: "文明库最早建设于"启辉计划"后，以时间为索引，记载文明中发生的一切事物。它能够实现"复原"功能：当文明被摧毁时，文明库的力量将使新的文明快速恢复到某一被记录的阶段。",
      icon: "info",
      button: "知道了",
    });
  });
})();
</script>
```

## 排版建议

1. **每个重要术语建议添加一个弹窗**，默认填入一个通用的解释模板，供用户后续修改
2. **弹窗按钮放在术语首次出现处**，方便读者及时了解
3. **弹窗正文不宜过长**，控制在100-200字以内
4. **使用emoji图标前缀**增加按钮的视觉吸引力（如 🎯、📚、⚡、🌟、🔮等）
5. **按钮文字格式**：`<emoji> 点我了解：<术语名称>`

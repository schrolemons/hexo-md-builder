# 维护与检查

[返回项目说明](../README.md)

## 本地检查

Python 3用于仓库检查；PPT模块校验另需Node.js。

在仓库根目录运行：

```sh
python .github/scripts/check_repository.py
```

仓库检查核对引用文件、JSON与Python语法；不代替实际内容审核、最终页面检查或演示文稿渲染。

## 发布与下载

在Actions手动运行“Skill package”，可下载当前提交的ZIP与SHA-256校验文件；这只是源文件快照，不会创建Release或新的版本号。下载后仍需按SKILL.md使用。

## 反馈

使用[Issues](https://github.com/schrolemons/hexo-md-builder/issues)报告问题，提供使用环境、操作步骤和预期／实际结果。日志中的密钥、账号、聊天记录与个人配置应先移除。已有仓库规则和安全说明优先于个人账号的通用模板。

## 项目标识

`docs/assets/project-cover.svg`是封面源文件，PNG用于README和链接分享。封面是项目标识，不是实际运行截图。版式由schrolemons的项目封面统一约定组成；修改时保留文字可读性和1280×640画布。

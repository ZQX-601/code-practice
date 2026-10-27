# Coding Interview Coach

这是一个面向 Meta 和字节跳动推荐算法岗位的 Codex Coding 教练项目。仓库同时保存：

- `skills/coding-interview-coach/`：Codex Skill 源码、教学规则和状态脚本。
- `coding/`：个人课程、题库索引、掌握度、错题和每日训练记录。

训练语言为 Python，默认采用 12 周课程、每天 90 分钟、一次一题的自适应训练方式。

## 在新电脑上使用

先安装并登录 Codex，然后执行：

```bash
git clone https://github.com/ZQX-601/code-practice.git
cd code-practice
./scripts/install-skill.sh
```

随后使用 Codex 打开该项目，并输入：

> 开始今天的训练

Agent 会读取 `coding/` 中的历史状态，从之前的进度继续。

## 日常同步

训练结束后，把 `coding/` 中新增的题目、评审和进度提交并推送到 GitHub。在另一台电脑开始训练前先执行 `git pull --ff-only`。

不要在两台电脑上同时进行训练并分别修改进度文件，否则可能产生 Git 冲突。

Skill 规则发生更新后，重新运行 `./scripts/install-skill.sh`。脚本会先备份已有的同名 Skill，再安装仓库中的版本。

## 安全边界

仓库不应保存 LeetCode 密码、Cookie、浏览器配置、API Key 或其他凭据。题库仅保存链接、标签、原创摘要和来源信号，不复制付费内容或完整题解。

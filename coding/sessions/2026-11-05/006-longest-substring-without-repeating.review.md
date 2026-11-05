# LC3 Longest Substring Without Repeating Characters 评审

- 首次快照：`coding/sessions/2026-11-05/006-longest-substring-without-repeating.py`
- 修正版：`coding/sessions/2026-11-05/006-longest-substring-without-repeating-v2.py`
- 评审日期：2026-11-05

## 结果

独立形成正确的动态区间实现。首次提交缺少 `defaultdict` 导入，在独立 Python 环境触发 `NameError`；修正版补齐导入，算法未改变。

## 证据

- 正确性：11 个定向用例通过，覆盖空串、全部重复、交错重复、重复字符位于窗口内部和空格。
- 随机验证：5000 个随机字符串与暴力参考实现对拍通过。
- 核心不变量：每轮收缩结束后，`s[start:end+1]` 中没有重复字符；旧窗口原本有效，因此加入右端字符后只有该字符可能导致冲突。
- 时间复杂度：首次回答 `O(n log n)`；经讲解后理解 `end` 和 `start` 均只单向移动、总移动次数各不超过 `n`，摊还时间为 `O(n)`。
- 空间复杂度：`O(k)`，其中 `k` 为字典中的字符种类数，最坏 `O(n)`。
- Python 完整性：首次遗漏 `from collections import defaultdict`，修正版已修复。
- 自测、dry run 和实际用时：未提交。
- 最高算法提示等级：0；复杂度分析接受了教练解释。
- 错误类别：`python_usage`、`complexity_not_acceptable`。

结论：标准题可独立完成

## 下一步

- 延迟复习时不查看旧代码，独立说明为什么嵌套 `while` 的总执行次数仍为 `O(n)`。
- 后续使用不同题面的连续区间变体验证迁移能力。
- 复习日期：2026-11-08、2026-11-12、2026-11-19、2026-12-05。

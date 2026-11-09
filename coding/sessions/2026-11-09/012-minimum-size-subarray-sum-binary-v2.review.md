# LC209 前缀和 + 二分版本评审

- 提交：`coding/sessions/2026-11-09/012-minimum-size-subarray-sum-binary-v2.py`
- 日期：2026-11-09
- 类型：完整讲解后的修正版本

## 结果与证据

- 修正后的代码正确：`prefix` 长度为 `n + 1`，二分结果是前缀数组下标，因此存在解的判断应为 `right < len(prefix)`。
- 手写 `bisect_search` 正确实现 lower bound：在 `[idx, len(prefix))` 中寻找第一个大于等于 `target` 的位置，无解时返回 `len(prefix)`。
- 固定 `left` 后搜索第一个 `prefix[right] >= prefix[left] + target`；最早的 `right` 给出该左边界下的最短合法子数组。
- 长度为 `right - left`，因为前缀下标描述半开区间 `nums[left:right]`。
- 定向边界用例与随机差分测试通过。
- 时间复杂度 `O(n log n)`：构造前缀和 `O(n)`，随后对 n 个左边界各做一次 `O(log n)` 二分。空间复杂度 `O(n)`。
- 第一版把 `right` 与 `len(nums)` 比较，漏掉了合法的前缀下标 `n`；经反例定位并讲解后修正。
- 最高提示等级：5；前缀和不等式、lower bound 的职责和完整实现均经过教学，本次不计独立完成。
- 错误类别：`boundary_or_initialization`。

结论：需要相似题强化

## 下一步

- 保留已安排的 LC209 间隔复习：11-10、11-12、11-16、11-23、12-09。
- 复习时先隐藏本次代码，分别验证滑动窗口的摊还分析和“前缀和 + 第一个满足阈值的位置”的迁移能力。

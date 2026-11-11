# LC238 除自身以外数组的乘积复习评审

- 提交快照：`006-product-except-self-review-submission.py`、`006-product-except-self-review-v2.py`
- 评审日期：2026-11-11
- 类型：第二阶段间隔复习

## 结果与证据

- Level 1 诊断后将方法从“双指针”修正为前缀/后缀累计，并将暴力时间修正为 O(n²)。
- 第一版独立写出左右累计数组实现，第二版进一步独立写出复用输出数组的 O(1) 额外空间实现。
- 两个版本分别通过 6 个定向用例和 5000 个随机差分用例，包括一个零、两个零、负数和单元素。
- 第一趟结束后 `ans[i] = product(nums[0:i])`；反向处理 i 之前，`right_product = product(nums[i+1:n])`。
- 反向更新必须先执行 `ans[i] *= right_product`，再把 `nums[i]` 纳入 right_product，否则会把当前元素错误乘进自己的答案。
- 时间复杂度 O(n)；第二版除输出数组外额外空间 O(1)。
- 初次把反向不变量写成 `nums[i:n]`，经 Level 1 的末尾空区间反例后确认应为 `nums[i+1:n]`。
- 未提供自生成测试、实际用时和提示声明。
- 最高提示等级：1。
- 错误类别：`pattern_not_recognized`、`boundary_or_initialization`。

结论：已通过短期掌握验证

## 下一步

- 完成 11-11 的 stage 2 任务；保留 11-15、11-22、12-08 后续复习。
- 后续先明确半开区间不变量，再写更新顺序，避免靠模板记忆。

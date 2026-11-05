# 错误模式记录

按概念错误聚合，不按题目数量堆积。每条记录应包含日期、题目、证据、错误类型、修正方法和复测结果。
## 2026-11-04
- LC217：将集合空间误判为 O(log n)。类别：complexity_not_acceptable。修正：无重复时保存 n 个元素，因此 O(n)。待 11-05 独立复测。
- LC1：口述 [0,1]，实际代码返回 [1,0]；两者均合法。尚未验证先查后存的解释。
- LC383：将两个先后执行的循环误判为 O(mn)。类别：complexity_not_acceptable。修正：顺序执行相加，嵌套执行才相乘；已当场正确复述，待延迟复测。
- LC205：未能独立形成一一映射检查方法，接受等级 5 完整讲解。类别：concept_not_understood。修正：同时检查正向和反向映射；使用 LC290 做相似题强化。
- LC290：空间复杂度回答 O(k)，漏算 `s.split(" ")` 创建的单词列表与字符串。类别：complexity_not_acceptable。修正：分析所有额外容器；已能说明同时存在的空间相加为 O(n+k)，再由高阶项化简为 O(n)，待延迟复测。
- LC125：第一版字符过滤判断较冗长，未主动提交复杂度、自测和提示声明；随后在 Level 4 结构提示下完成双指针版本。类别：python_usage。修正：理解 `isalnum()`、半开区间和外侧有效字符已配对的不变量；待 11-06 无提示复测。
- LC3：首次遗漏 `defaultdict` 导入，并因 `while` 写在 `for` 内将时间误判为 O(n log n)。类别：python_usage、complexity_not_acceptable。修正：内层指针不重置且只单向移动，所有 while 总次数最多 n，因此总时间 O(n)；待 11-08 独立复述。

## 2026-11-05
- LC217：复杂度使用未定义 k，并混淆提前返回与最坏情况；complexity_not_acceptable。代码独立正确，复杂度待复测。
- LC49：已知 set 不可作为键，但 initially 未提及集合丢失频次；concept_not_understood。已解释 abb/ab，后续用计数 tuple 检查理解。

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

## 2026-11-07
- complexity_not_acceptable：290 再次忽略 split 空间，讲解后仍答 O(1)，未通过，后续用小例子复测。49 漏算各组26元组；242 固定字母集空间应 O(1)；复杂度符号要定义。
- pattern_not_recognized：128 起点判定、560 前缀和计数需完整讲解，后续独立复测。560 暴力扩展曾把 nums[right] 写成 nums[left]。

## 2026-11-08
- 560：counts不是子数组数量，而是旧前缀和频次；空间O(k)误用目标k，最坏O(n)。
- 303：right+1闭区间边界首次答错；仅引用原数组不是复制，朴素版额外空间O(1)。含当前/不含当前两种前缀定义不可混用。
- 238：接受完整讲解后完成；右积先用于答案再纳入当前元素。

## 2026-11-09
- LC125：代码与 O(n)/O(1) 独立复写正确，但只用“避免越界”解释 `right - 1`，未完整表达 `[left,right)` 半开区间；不变量回答过于笼统并跳过复述。后续复习继续验证解释能力。
- LC205：双字典实现正确，但不能独立说明反向字典用于阻止多个源字符映射到同一目标字符；经 `ab -> aa` 反例解释后理解。类别：concept_not_understood；11-11 继续无提示复测。
- LC217：11-09 延迟复习中代码、最坏复杂度和集合不变量全部独立回答正确；此前的 complexity_not_acceptable 已通过短期验证，仍保留后续长期复习。
- LC3：11-09 复习前查看过旧记录，不计独立；能给出 O(n) 结论，但只能模糊说明 while 不会完整遍历。需记住 start 不回退、所有 while 总次数最多 n 的摊还证明。类别：complexity_not_acceptable。
- LC209：滑动窗口代码正确，但 O(n) 理由仍停留在 while 不会完整遍历；应说明 left/right 各自最多移动 n 次。能识别负数使 total 不单调，需进一步说明移入负数可能减和、移出负数可能增和。类别：complexity_not_acceptable。
- LC209 前缀和 + 二分：第一版用 `right < len(nums)` 判断二分是否找到结果，漏掉合法的前缀下标 `n`。类别：boundary_or_initialization。修正：二分搜索的是长度为 `n+1` 的 `prefix`，所以应判断 `right < len(prefix)`；修正版已通过测试，待隐藏旧解复测。

## 2026-11-10
713 漏 k=1。固定右端计数时，和 < k 加窗口长度，和 >= k 加已排除的起点数 left。后者首次在 while 内逐个累加，漏掉以前移出的起点。
- LC3：第三次能给出 O(n) 结论，但仍未独立陈述 `left` 不回退且所有 while 总次数最多 n 的摊还证明，本次选择跳过。类别：complexity_not_acceptable。代码与窗口无重复条件正确，11-12 继续验证解释能力。
- LC49：排序键代码正确，初答时间 O(nk) 漏掉每个长度 k 字符串的排序成本；Level 1 追问后自行修正为 O(n*k log k)。类别：complexity_not_acceptable；本次已当场修正，后续复习检查能否一次答对。
- LC724：首次回忆时表示忘记，经 Level 1 暴力定义提示后自行恢复 O(1) 空间优化。类别：pattern_not_recognized。能正确说明 `left_sum` 是不含当前元素的 `nums[0:i]`，下一轮应无需提示直接推导。
- LC525：首次到期复习依赖查看旧提交，不能作为记忆证据；随后能正确解释 balance、相同状态的差为 0、保留最早下标及 O(n)/O(n)。类别：pattern_not_recognized、variant_transfer_failure。用 LC560 检查相近结构的独立迁移。
- 前缀和检索失败：LC525、LC560 均表现为查看旧解后立即理解，但隐藏旧解时无法从题意恢复方程。类别：pattern_not_recognized、variant_transfer_failure。修正：先写 `P[right]-P[left]=目标`，再移项求需要的旧状态；根据“是否存在/多少个/最长”分别选择集合/频次/最早下标，使用短推导和间隔复测替代重复抄模板。

## 2026-11-11
- LC128：因题目不是连续区间而误归类为双指针；实际没有两个协调移动的指针，核心需求是 O(1) 平均存在性查询，应识别为哈希结构。初始 O(n) 理由不精确，经 Level 1 后能说明每个不同数字最多被一条序列扩展一次。类别：pattern_not_recognized、complexity_not_acceptable。
- LC238：初始误归类为双指针，实际是前缀/后缀累计；反向变量初答包含当前元素 `nums[i:n]`，正确不变量是处理 i 前保存 `nums[i+1:n]`。经 Level 1 空区间反例修正。类别：pattern_not_recognized、boundary_or_initialization。
- LC303：已能识别前缀和，但闭区间查询再次写成 `prefix[right]-prefix[left]`，漏掉 right；经单元素反例修正为 `prefix[right+1]-prefix[left]`。类别：boundary_or_initialization。后续必须先写 `prefix[i]=sum(nums[0:i])` 再推导。

## 2026-11-11
904 每轮重建 set、收缩时切片导致最坏 O(n²)。固定右端计数时严格小于阈值应排除和恰好等于阈值的区间。

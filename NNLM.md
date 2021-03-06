---
title: 神经网络语言模型-NNLM
date: 2016-09-17 12:25:45
categories: Machine Learning
tags: 
- Neural Nework
- Machine Learning
- Deep Learning

---

作者：[一个独行的程序员](https://cn.linkedin.com/in/jingtianp)

*Bengio 2003年的NNLM可谓是神经网络语言模型的开山之作，并且为后来的Word2Vec、RNNLM、NMT等提供了思路，为DL4NLP打下了坚实的基础。*

## 语言模型

通俗的说，语言模型就是判断一句话像不像是人说出来的。
形式化的定义，语言模型是借由一个概率分布，试图用概率p(s)来表示字符串s作为1个句子出现的频率：
$
    p(s) = p(w_1,...w_m)
$

<!-- more -->

语言模型在许多NLP相关的问题都有应用，如语音识别、机器翻译、词性标注、句法分析和信息检索等。
然而，如果通过穷举的方式枚举所有的w来计算p(s)，时间和空间代价都是巨大的。
假设词汇表单词数V = 10000，句子平均长度为M = 20，则时间复杂度为$O(V^M)$，即$O(10^80)$。因此，我们常常使用**n-gram**模型来近似求解p(s)。

## n-gram 语言模型

对于一个由M个词构成的句子$s=w_1w_2...w_M$，其概率计算公式为：

$
    p(s) = p(w_1)p(w_2|w_1)p(w_3|w_1w_2)...p(w_t|w1...w_{M-1})
         = \prod_{i=1}^{M} p(w_i|w_1...w_{i-1})
$

产生第i个词的概率是由已经产生的i-1个词$w_1w_2...w_{i-1}$决定的。n-gram模型则是只考虑已经产生的前n-1个单词，而不是从句首开始的所有单词。因此，公式变为：

$
    p(s) = \prod_{i=1}^{M} p(w_i|w_i-n+1...w_{i-1})
         = \prod_{i=1}^{M} p(w_i|w_{i-n+1}^{i-1})    
$

在实际建模时，考虑到计算时间，我们常常取n=2或n=3，即bigram或trigram。

## Bengio的NNLM

相对于统计语言模型，NNLM在相似语义（similar semantic）和语法角色（grammatical roles)上进行了优化。首先看一个例句：

"The cat is walking in the bedroom"

通过NNLM可以产生类似的句子，如：

"A dog was running in a room"

因为两句话中的(the, a)、(room, bedroom)、(dog, cat)等词对拥有相似的语义和相同的语法角色，所以才能构造出相似的句子。

同时，NNLM通过分布式表示（distributed representations）解决了维度灾难（curse of dimensionality）的问题。通过词向量矩阵C，将词汇表中的V个单词映射为V个m维的词向量（feature vector）。

同样使用n-gram表示，但是NNLM却是共享参数矩阵C。相反，统计语言模型却需要用词矩阵表示每一个句子，空间代价太大。


Bengio通过1个3层的神经网络来构建NNLM，并且与普通NN不同的是：输入层的输入数据实质上是词向量矩阵C，并且是全局共享的。

为了说明，下面定义符号：
训练集是许多由词$w_1...w_T$构成的句子，其中$w_t \in V$，词汇表V是有限个不重复词组成的集合。训练目标是学到一个很好的模型:

$f(w_t,...,w_{t-n+1})=\hat p(w_t|w_1^{t-1})$

取 $\frac{1}{\hat p(w_t|w_1^{t-1})}$ 的几何平均值作为困惑度（*perplexity*）,即log似然的几何平均的指数。

模型中的唯一常数是对于任意的组合$w_1^{t-1}$,保证

$\sum_{i=1}^{|V|} f(i,w_{t-1},...,w_{t-n+1}) = 1, \quad  f > 0$。

通过条件概率的乘积，我们能够得到许多词组合成句子的联合概率。将

$
f(w_t,...,w_{t-n+1})=\hat p(w_t|w_1^{t-1})
$

分解成两部分：
    
1. 词汇表V中的第i个单词->词向量$C(i) \in R^m$。 C(i)表示每个词i的分布式词向量(distributed feature vector),C是一个拥有$|V| x m$参数的词向量矩阵。
2. 第i个词的上文的向量形式为：$(C(w_{t-n+1}),...,C(w_{t-1}))$,已知词汇表V中第i个词在已知前n-1个词时的条件概率是$p(w_t|w_1^{t-1})$，定义函数

	$
	g(i,C(w_{t-n+1}),...,C(w_{t-1}))为此时第i个词的词向量，即：
	$

	$
	    f(i,...,w_{t-n+1}) = g(i,C(w_{t-n+1}),...,C(w_{t-1}))
	$

因此，函数f是C和g的复合函数，并且C是所有词共享的一个参数矩阵。函数g可以用一个前馈网络(FNN)或循环神经网络(RNN)来实现，设网络中所有参数为$\omega$。则整个NNLM的参数$\theta = (C,\omega) $。

模型的训练目标：

$
    \mathop{argmax}_{\theta} L = 1/T \sum_{t}^{|V|} log f(w_t,...,w_{t-n+1}; \theta) + R(\theta)
$

其中$R(\theta)$为正则化惩罚项。

{% asset_img nnlm1.png 神经网络语言模型 %}


输入层：将$C(w_{t-n+1}),...,C(w_{t-1})$这n-1个词向量首尾相接拼起来形成一个$(n-1)m$维的向量x。

隐藏层：输入$o=d+Hx$，d为$h$维的隐层偏置项，H为$h x (n-1)m$维的隐层参数；输出$a=tanh(o)$

输出层：用Softmax做V分类，模型大部分计算都在这一层；$y_i$表示下一个词为i的未归一化log概率：

$
    y = b + Wx + U tanh(d+Hx)
$

其中，U为$|V| \times h$维的输出层参数矩阵，b为$|V|$维的输出层偏置项。模型考虑了从输入层直接到输出层的概率，W即为输入层直连输出层的$|V| \times (n-1）m$维参数矩阵。

综上：$\theta = (b,d,W,U,H,C)$，

总参数个数为:$|V|(1+mn+h)+h(1+(n-1)m)$。

用随机梯度上升求解：

$
    \theta \rightarrow \theta + \epsilon \frac {{\partial log{\hat P(w_t|w_{t-1},...,w_{t-n+1})}}} {\partial \theta} 
$

# 平台架构分析

在 [平台基础分析]() 中我们介绍了TensorFlow的基本运作方式，包括Graph、Session、Variable、Tensor等基础类的结构和作用。

本篇教程会从平台架构层面分析TensorFlow的控制流、数据流、功能模块、运行时环境、计算图切分等。

* [控制流](#control-flow)
    * [单机控制流程分析](#local-controlflow)
    * [分布式控制流程分析](#distributed-controlflow)
* [数据流](#data-flow)
* [功能模块图](#functional-module)
* [运行时环境](#runtime)
    * [单机](#common-runtime)
    * [分布式](#distributed-runtime)
* [计算图切分](#graph-partition)
    * [第一阶段](#server-level)
    * [第二阶段](#device-level)


<h1>
  <a id="control-flow" class="anchor" href="#control-flow"></a>控制流
</h1>

<h2 id="local-controlflow">单机控制流程分析</h2>


<h2 href="#distributed-controlflow">分布式控制流程分析</h2>

<h1 href="#data-flow">数据流</h1>

----------


<h1 href="#functional-module">功能模块图</h1>

<img src="imgs/framework0.png" width="40%" height="35%" >

----------

###### runtime

<h1 href="#runtime">运行时环境</h1>

<h2 href="#common-runtime">单机</h2>

<h2 href="#distributed-runtime">分布式</h2>

----------


<h1 href="#graph-partition">计算图切分</h1>


----------



**返回：**[主目录](tensorflow/h3doc/readme.md)

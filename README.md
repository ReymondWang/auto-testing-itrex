**目标：** 本项目专注于解决WEB系统测试领域中，基于GUI测试技术的PO对象自动化生成。（PO，即页面对象，在自动化测试领域通常用来封装单个页面的控件对象及操作。）

**模型：** Intel发布的neural-chat-7b-v3-1对话模型。

**软件环境：** intel-extension-for-transformers1.4.2-dev，neural-speed1.0，neural-chat的server及client，selenium 4.18.1，Chrome124.0.6367.62。

**基础环境：**
<table>
  <tr>
    <td colspan="2">服务端</td>
  </tr>
  <tr>
    <td>CPU</td>
    <td>Xeon(R) Gold 6430</td>
  </tr>
  <tr>
    <td>内存</td>
    <td>64G</td>
  </tr>
  <tr>
    <td>操作系统</td>
    <td>Ubuntu 22.04</td>
  </tr>
  <tr>
    <td colspan="2">客户端</td>
  </tr>
  <tr>
    <td>CPU</td>
    <td>Intel Core i7 六核</td>
  </tr>
  <tr>
    <td>内存</td>
    <td>16G</td>
  </tr>
  <tr>
    <td>操作系统</td>
    <td>macOS Ventura 版本13.6.6</td>
  </tr>
</table>

**实现思路：** 利用大模型的文本理解和代码生成能力，将WEB页面的框架元素和设计过的Prompt模版结合起来作为输入，并从返回结果中解析出适合的Python代码。

**系统的整体结构如下：**

<img width="415" alt="image" src="https://github.com/ReymondWang/auto-testing-itrex/assets/13266952/462962ba-488f-4fb0-8578-e134ee9fb354">


**系统启动命令：**
```python
conda activate itrex

python crawler/hs_crawler.py 
```

**系统统一的配置文件：**
```python
./config/crawler.yml
```
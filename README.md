# 基于 hsv 的马赛克拼图效果
<br>

[![Build Status](https://travis-ci.org/NoisyWinds/puzzle.svg?branch=master)](https://travis-ci.org/ThomasHuai/puzzle)

<br>

文章链接：[利用爬虫技术能做到哪些很酷很有趣很有用的事情？](https://www.zhihu.com/question/27621722/answer/269085034)

<br>

## 2018-5-30 更新内容
- 修复了生成失败中断的问题
- 不再读取数据库中的非图片文件
- 自定义最低相似标准 -far （默认1000）
- 修复命令行参数类型错误（竟然没人发现）。。。
- 爬虫依旧有效

## 2018-4-20 更新内容
- 修复抓取路径到 2018-4-20 可用
- 使用 ImagesPipeline 下载图片
- 抓取时不处理图片（对应一些人想要原图的要求）
- 考虑到 opencv 库比较难安装，处理图片改为使用 Pillow（PIL）库。
- 请勿占用站长大量带宽，谢谢。

<br>
 
## 一、安装环境 （python3.6 or upper）


### 1.安装 Scrapy 爬虫框架  (install Scrapy 1.4 upper)  

<br>

`pip install Scrapy`

<br> 

推荐使用whl进行安装 [点击此处](https://www.lfd.uci.edu/~gohlke/pythonlibs/)  

<br>

### 2.安装 numpy 科学计算库 (install numpy) 

<br>

`pip install numpy`  

<br>

### 3.安装 Pillow 图像处理库 (install Pillow)

<br>

`pip install Pillow`  

<br>

 推荐使用 wheel 来安装 Pillow [点击此处]("https://www.lfd.uci.edu/~gohlke/pythonlibs/") 

<br>

<br>
 
## 二、使用 puzzle 生成拼图 （use puzzle.py create mosaik puzzle） 

<br>

### 爬取图片（catch images）

* 图片默认存储路径是 database/full 文件夹，图片名为hash值
* 自定义路径请在 setting.py 中进行修改
* 自定义文件名请在 pipelines.py 中重构 ImagesPipeline 类

<br>

`python run.py`  or ``scrapy crawl images` or run catchImage.bat

<br>

### 创建拼图图片 （create puzzle image）  

<br>
- 注意，路径后面要有反斜杠
`python puzzle.py -i test.jpg -d D:/acg/img/ -o output/`  or run start.bat

<br>

### 命令行参数说明（Command line parameters）

<br>

* -s -- save  已经存在output文件夹已经有马赛克图片，快速生成图片 Created faster when there have  mosaik pictures
* -i -- input 原始图片路径 input image path
* -d -- database 爬虫图片数据集 your image database
* -o -- output 马赛克图标生成路径 output mosaik pictures path
* -is -os 输入（马赛克块）/ 输出（生成图） 图片尺寸  input size / output size
* -r --repate（int） 重复（建议在图片集少的时候设置） mosaik repate (When image is not enough)
* -far --far（int） 相似度（可以在无法构造图片的时候适当增大，默认1000） masaik difference

<br>
 
<br>

<br>

test.jpg  

<br>

![image](./test.jpg)  
<br>

output jpg  
<br>

![image](./out.jpg)  

<br>

# 已知问题
- 少数图片，图片后缀名错误，比如说jpg图片修改后缀名为png进行伪造将会影响 Pillow 读取像素信息。（4-20 更新已经跳过影响图片）
- 效果较差的原因有可能是，图片集数量不够（建议5000之内设置重复），黑白构图图片太多会直接影响 hsv 结果，图片单一，无法就近匹配。
- 更多优化建议，bug信息请在评论区回复，感谢支持。



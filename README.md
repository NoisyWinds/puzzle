# 基于 hsv 的马赛克拼图效果  
## 一、安装环境  
### 1.安装 Scrapy 爬虫框架  (install Scrapy)  
`pip install Scrapy`  
windows 安装可以 [点击此处](https://sourceforge.net/projects/pywin32/)  
推荐使用 wheel 来安装 opencv [点击此处](https://www.lfd.uci.edu/~gohlke/pythonlibs/)  
### 2.安装 numpy 科学计算库 (install numpy)  
`pip install numpy`  
### 3.安装 Pillow 图像处理库 (install Pillow)  
`pip install Pillow`  
 推荐使用 wheel 来安装 Pillow [点击此处]("https://www.lfd.uci.edu/~gohlke/pythonlibs/")  
## 二、使用 puzzle 生成拼图 （use puzzle.py create mosaik puzzle）  
### 爬取图片（catch images）  
`Scrapy craw images`  
### 创建拼图图片 （create puzzle image）  
`python puzzle.py -i test.jpg -d D:/acg/acg/img/ -o output/`  
### 命令行参数（Command line parameters）  
* -s -- save  已经存在output文件夹已经有马赛克图片，快速生成图片 Created faster when there have  mosaik pictures
* -i -- input 原始图片路径 input image path
* -d -- database 爬虫图片数据集 your image database
* -o -- output 马赛克图标生成路径 output mosaik pictures path
* -is -os 输入（马赛克块）/ 输出（生成图） 图片尺寸  input size / output size
* -r --repate（int） 重复（建议在图片集少的时候设置） mosaik repate (When image is not enough)  
test.jpg  
![image](./test.jpg)  
output jpg  
![image](./out.jpg)  



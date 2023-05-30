针对AndroidManifest.xml文件批量进行检查：

1.逆向或解压app，找到AndroidManifest.xml文件；

2.为了方便检查完快速找到对应的、存在漏洞的app，可以用"app的名字.xml"命名后

存放在apks文件夹；

3.运行脚本

```
python3 appTruck.py
```











先把坑挖上，1.0.2版本将针对终端输出信息保存为文本或者表格做优化
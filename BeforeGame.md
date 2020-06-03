#Question
Apache 默认端口号80
XProbe2通过 模糊签名猜测，可能性猜测 同时多匹配和签名数据库来识别操作系统


# 配置网卡信息 #
```
配置文件 nano /etc/network/interfaces

iface eth0 inet static           //配置eth0使用默认的静态地址
address 172.30.1.160        //设置eth0的IP地址
netmask 255.255.0.0        //配置eth0的子网掩码
```
采用静态IP地址的方式，还需要手动设置DNS配置文件，在终端中输入命令
```
nano /etc/resolv.conf
```
输入DNS地址，上述都设置完毕后，重启一下系统
# SSH and Apache #
## 配置SSH ##
```
nano /etc/ssh/ssd_config
```
去掉注释
```
#passwordAuthentication yes
```
开启服务
```
service ssh start
/etc/init.d/ssh start
```
## 配置Apache ##
配置文件
```
nano /etc/apache2/ports.conf 修改默认端口号
```
开启服务
```
service apache2 start
/etc/init.d/apache2 start
```
# 渗透测试过程 #
- 第一步：目标范围划定
- 第二步：信息搜集
- 第三步：目标发现
- 第四歩：目标枚举
- 第五步：漏洞映射
- 第六步：社会工程学
- 第七步：漏洞利用
- 第八步：提权
- 第九步：持续控制目标
- 第十步：文档和报告

# W3af_consle #
|方式|作用|
|-|-|
|view |查看参数|
|set| 改变参数值|
|back |返回上一级|
|help |查看帮助|

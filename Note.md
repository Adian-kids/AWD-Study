# 待办
准备不死马
准备文件监控脚本
准备流量监控脚本
准备批量POC
# Reference
> Vedio Link:https://www.bilibili.com/video/BV1Tz4y197fF      
> https://zhuanlan.zhihu.com/p/48987615
# 注意事项
1.注意Check避免持续扣分
2.注意流量监控，文件监控日志
3.注意不要宕机，疯狂扣分
# Defense
## 备份网站源码以及数据库
```
mysqldump -u root -h host -p dbname > backdb.sql
```
## 弱口令加固
修改密码
```
passwd username
```
弱口令被建立Sessions除非重启否则不会断开，非root无权限重启，所以持续后门维持
```
cat /etc/passwd 
``` 
查看所有账户信息（/bin/bash为可登录账户）,若存在其他可登录账户
```
su Username
```
切换账户更改密码

## 后门修复
### 查看开放端口
```
netstat -stl(TCP)
netstat -nul(UDP)
``` 
>  Local Address 0.0.0.0则可以任何人连接 0.127.0.0则仅限本地连接，比如3306端口（mysql）  
### Web后门查找
1.根目录下文件名不正常的文件 `aaa.php` `abc.php ` `bkd.php`等等   
查看隐藏文件
```
ls -l
```
2.从当前目录下查找危险函数（用处不大，难以寻找）
```
grep "eval" -R ./*
```
3.将代码下载下来查杀,打包到Web根目录下
使用Winscp Cooy到本地
```
zip  -r fileName.zip  文件夹路径（/home/www）
tar czvf filename.tar 文件夹路径（/home/www）
```
查找网站根目录位置
```
find / -name index.php
```
### 不死马防护
注释掉内容，重新给变量赋值
## Web基础防护
1.修改默认账户密码（更改数据库，md5）
2.代码审计查找其他漏洞,注意检查日志，可能会有写入的一句话
## 关闭Mysql外部连接
```
use mysql;
update user set host = “localhost” where user = “root” and host= “%”;
flush privileges;
```
# Attack
## 弱口令攻击
对手未更改默认密码或者存在其他账户，可以使用Msfconsole中的ssh_login模块去进行弱口令攻击
> ssh_login模块可以设定ip段作为目标 Example: 172.16.1.1-172.16.1.10 or 172.16.1-10.102


查看已创建的Sessions
```
sessions
```
连接对方的服务器
```
sessions -i Id
```
查看flag
```
cat /flag*
```
## 官方后门批量
可能会有官方存下来的Webshell，短文件名等都要注意，即使查杀使用脚本批量
## 根据系统版本提权（初始非root情况）
```
cat /proc/version
```

## 高权限添加开机启动项,循环重启等
```
nano /etc/rc.local
```

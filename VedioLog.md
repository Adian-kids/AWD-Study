# Reference
> Vedio Link:https://www.bilibili.com/video/BV1Tz4y197fF
# Defense
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
1.根目录下文件名不正常的文件 aaa.php abc.php bkd.php等等   
查看隐藏文件
```
ls -l
```
2.从当前目录下查找危险函数（用处不大，难以寻找）
```
grep "eval" -R ./*
```
3.将代码下载下来查杀


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
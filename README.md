# 东北大学IP网管登录注销脚本
## 使用
- 将`config-sample.ini`重命名为`config.ini`
- 修改`config.ini`文件内用户名和密码
- 运行脚本
    - 登录
    - 注销
## 登录
```shell
python3 login.py        # PC端登录
python3 login.py phone  # 移动端登录
```
## 注销
```shell
python3 logout.py
```
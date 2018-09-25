参考资料:
http://www.liujiangblog.com/blog/36/

运行步骤:
1.创建Django项目

2.创建新模块 命令行输入 login模块创建
python manage.py startapp login

3.运行命令:
python manage.py runserver 127.0.0.1:8000
或者
在editconfiguration中配置运行

4.还有使用sqlite3数据库
python manage.py makemigrations
python manage.py migrate

效果:
1.访问http://localhost:8000/index 主页

2.访问http://localhost:8000/login登陆-->到index 有了刚刚登陆信息

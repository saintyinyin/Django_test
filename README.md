# python option
    {
    -B： 是否生成相应的 `pyc` 文件
    -c cmd：执行字符串命令 `cmd`
    -d：启用调试
    -E：忽略所有的 `PYTHON*` 环境变量
    -I：忽略用户自己的环境信息，包括
    -O：生成的 `pyc` 文件不包含 `assert` 语句和 `__debug__` 信息
    -OO：在 `-O` 的基础上，进一步忽略代码的一些注释字符串
    -q：交互式模式下不显示 Python 的版本和版权信息
    -s：排除用户自己安装的 Python 模块
    -S：在启动 Python 的时候不导入模块 `site`
    -v：打印更多的代码执行的相关信息
    -V：打印 Python 解释器的版本号
    -W arg：警告的相关控制参数
    -x：跳过代码里面的第一行（`#!cmd`）
    -X：一些 Python 代码执行时的参数控制
    --check-hash-based-pycs：设置是否对 `pyc` 文件进行 hash 校验
}

####################################
# Django_test
Study django project and put all of them on github project Django_test

Outlines:
1. vscode env -- c:\users\scnzhy\.virtualenvs\django
   . cd <env>/Scripts
   . activate (enter django env)
2. django
   . django-admin startproject bookmanager # Create project
       {
        1) manage.py文件
          一级子目录中的 manage.py 文件是管理 Django 项目的重要命令行工具，它主要用于启动项目、创建应用和完成数据库的迁移等。
        2) __init__.py文件
          二级子目录中的 __init__.py 文件用于标识当前所在的目录是一个 Python 包，如果在此文件中，通过 import 导入其他方法或者包会被 Django 自动识别。
        3) settings.py文件
          settings.py 文件是 Django 项目的重要配置文件。项目启动时，settings.py 配置文件会被自动调用，而它定义的一些全局为 Django 运行提供参数，在此配置文件中也可以自定义一些变量，用于全局作用域的数据传递。
        4) urls.py文件
          url.py 文件用于记录 Django 项目的 URL 映射关系，它属于项目的基础路由配置文件，路由系统就是在这个文件中完成相应配置的，项目中的动态路径必须先经过该文件匹配，才能实现 Web 站点上资源的访问功能。
        5) wsgi.py文件
          wsgi.py 是 WSGI（Web Server Gateway Interface）服务器程序的入口文件，主要用于启动应用程序。它遵守 WSGI 协议并负责网络通讯部分的实现，只有在项目部署的时候才会用到它。
        } 
   . python manage.py startapp book  # Create sub-app of django
       {
        admin.py 用于将 Model 定义的数据表注册到管理后台，是 Django Admin 应用的配置文件；
        apps.py 用于应用程序本身的属性配置文件；
        models.py 用于定义应用中所需要的数据表；
        tests.py 文件用于编写当前应用程序的单元测试；
        views.py 用来定义视图处理函数的文件；
        一级目录下的 __init__.py 文件标识 index 应用是一个 Python 包；
        migrations 目录用于存储数据库迁移时生成的文件，该目录下的 __init__.py 文件标识 migrations 是一个 Python 包。
        }
   . tree /f <dir>
   . http://127.0.0.1:8000/ # Access django website
   
   # ======ORM model===== #
   # Object Relational Mapping(关系对象映射)
      # 类名对应------》数据库中的表名
      # 类属性对应---------》数据库里的字段
      # 类实例对应---------》数据库表里的一行数据
      # obj.id  obj.name.....类实例对象的属性
   # Django的orm操作本质上会根据对接的数据库引擎，翻译成对应的sql语句；所有使用Django开发的项目无需关心程序底层使用的是MySQL、Oracle、sqlite....，如果数据库迁移，只需要更换Django的数据库引擎即可；
   . python manage.py makemigrations   # make migration file, convert class to table structure file
   . python manage.py migrate  # exec migrate, then db create tables

# history
   . Modified by zhigang.yin at 11Aug2021

# 清问问卷

#### 一款基于Vue2+Django3的问卷发布收集系统

有问题可以联系ethan_shao@qq.com

[前端项目地址](https://github.com/shaobaitao/clear_questionnaire/vue_clear_questionnaire)

[后端项目地址](https://github.com/shaobaitao/clear_questionnaire/django_clear_questionnaire)

[项目demo](http://qw.shaobaitao.cn) 

测试账号qw_7	密码Test1234

用到的一些东西

```
Vue2
Django3
Redis
Mysql

Vant
Element
```



### 实现的功能

```
问卷创建
问卷删除
问卷分析
问卷预览
问卷收集
问卷数据分析
问卷数据下载
用户邮箱注册登录
```



### 还需的功能

```
添加大量注释
添加动画
问卷题目重编辑功能
完善后端权限认证
状态码管理
图片系统
接口文档
部署文档
后台管理
```

### 简单开发环境安装文档

### 前端

node 12.18.0

```shell
git clone https://github.com/shaobaitao/vue_clear_questionnaire.git
```

```shell
cd vue_clear_questionnaire
```

```shell
npm install
```

```shell
npm run serve
```

后端接口地址修改 vue.config.js

### 后端

CentOS 7.9
python 3.8

```shell
git clone https://github.com/shaobaitao/django_clear_questionnaire.git
```

```shell
cd django_clear_questionnaire
```

```shell
pip install -r requirements.txt https://mirrors.aliyun.com/pypi/simple/
```
修改配置 带星号一定要修改 /django_clear_questionnaire/settings.py
```shell
python manage.py runserver 0:5000 
```

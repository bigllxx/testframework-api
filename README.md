## 手动运行
##### 运行环境：python3.x
##### 依赖安装：
> pip install -r requirements.txt
##### 安装allure：
> brew install allure
##### 执行脚本
> python run.py \<env>  # qa / test
##### 日志查看
> cat result/logs/all.log

## docker运行
##### 运行环境：bigllxx/centos-allure:1.8.0
##### 打包：
> docker build -t test_framework .
##### run：
> docker run -v /home/bigllxx/allure/allure_report:/usr/testframwork/result/report/allure --name test_framework test_framework
##### 测试报告：
> allure serve -p 7788 /home/bigllxx/allure/allure_report

## 配置测试报告邮件接受人
> 在config.ini -> receive_addr，后面添加邮箱，英文逗号隔开

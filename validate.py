import jenkins
#定义远程的jenkins master server的url，以及port
url = 'http://192.168.31.23:8080'
username = 'admin'
password = '2b51205602f8463fb81bbdc71a01cf94'

#构建job名为job_name的job（不带构建参数）
job_name = "job"

# 实例化jenkins对象
server = jenkins.Jenkins(url, username, password)

# # 获取下一项目构建号
#  next_build_number = server.get_job_info(job_name)['nextBuildNumber']
#获取job名为job_name的job的最后一次构建号
number=server.get_job_info(job_name)['lastBuild']['number']
# number='2'
print(number)
#
# # 构建项目
# output = server.build_job(job_name)
#
# # 定时10秒
# from time import sleep;
# sleep(10)

# flag=server.get_build_info(job_name,next_build_number)['building']
# print(flag)

# sleep(60)
# print(flag)
#获取job名为job_name的job的某次构建的执行结果状态

build_info = server.get_build_info(job_name, number)

status = build_info['result']

print(status)

if status == "SUCCESS":
    print("构建成功：%s | 构建项目编号：%s" % (job_name, number))
else:
    print("构建出错: %s" % job_name)

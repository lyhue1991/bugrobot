# bugrobot 微信报警机器人


Algorithm engineers or RDs often feel anxious when monitoring their running codes.

Some codes can be running for several hours and even be running for several days.

Such as the training of Deep Learning Models and some Big Data ETL tasks.

If we can send some important message about the running status to our email or wechat,

then we can know the status of our running task from our phone.

Wow, that will be a great bless to the rest hairs of our Algorithm engineers.

Actually, it can be achieved easily by send email with Python.

If we set QQ mail remind on wechat and sending emails to our QQ Email, we cat receive the messages on our phone.

Let's see how to do this!


算法工程师常常会为监控代码而头痛，有些代码执行时间常常会长达数小时，甚至几天。

例如一些机器学习模型的训练，以及一些大数据ETL任务。

如果能够将执行过程中的一些中间重要信息发送到我们的微信上，随时随地在手机上看到程序是否正常运行，让一切都在掌握之中，

那么将会让算法工程师的许多头发免受骨肉分离，随风飘零之苦。

实际上我们通过利用Python代码发送邮件到我们的QQ邮箱，并在微信上设置QQ邮箱提醒，可以非常容易实现这个功能。

效果如下，让我们来看看怎么做吧！


![](微信报警机器人.jpg)




```python
#setup bugrobot
!pip install bugrobot 
```

```python

```

```python
#enjoy!
```

```python
import  bugrobot

subject = "info@train_model.py" 
msg = "auc=0.98" 
receivers = ["2650115830@qq.com"] 

#①send message to Email!
bugrobot.send_msg(receivers,subject,msg)

#②send the bug information to Email if any exception occor!
def f():
    return 1/0
bugrobot.monitor_run(f,["2650115830@qq.com"])
```

```python

```

Algorithm engineers or RDs often feel anxious when monitoring their running codes.

Some codes can be running for several hours and even be running for several days.

Such as the training of Deep Learning Models and some Big Data ETL tasks.

If we can send some important message about the running status to our email or wechat,

then we can know the status of our running task from our phone.

Wow, that will be a great bless to the rest hairs of our Algorithm engineers.

Actually, it can be achieved easily by send email with Python.

If we set QQ mail remind on wechat and sending emails to our QQ Email, we cat receive the messages on our phone.

Let's see how to do this!


![](微信报警机器人.jpg)

```python

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

# encoding: utf-8
# Created my-pika by wym at 2018/9/30

"""
This is the cline end, implement the add function
"""
import pika

# 连接rabbitmq服务器
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()

# 定义队列
channel.queue_declare(queue='compute_queue')
print(' [*] Waiting for n')



# 将n值加1
def increase(n):
    return n + 1


# 定义接收到消息的处理方法
def request(ch, method, properties, body):
    print(" [.] increase(%s)" % (body,))

    response = increase(int(body))

    # 将计算结果发送回控制中心
    ch.basic_publish(exchange='',
                     routing_key=properties.reply_to,
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print(' [.] Response(%s)' % (response, ))

# 消息获取顺序（公平调度）
# 使用basic_qos设置prefetch_count=1，使得rabbitmq不会在同一时间给工作者分配多个任务，只有工作者完成任务之后，才会再次接收到任务
channel.basic_qos(prefetch_count=1)
channel.basic_consume(request, queue='compute_queue')

channel.start_consuming()

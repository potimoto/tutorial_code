import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')

        ##### ① #####
        
        ##############

        timer_period = 1  # 秒
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0 # 何回publishしたかを数えるカウンタ


    def timer_callback(self):
        twist = Twist()

        if self.i <= 10: 
            twist.linear.x = 0.05 # ロボットの並進速度．正の値であれば前進（単位m/s）
            twist.angular.z = 0.3 # ロボットの角速度．正の値であれば反時計回り（単位rad/s）
        else:
            twist.linear.x = 0.0
            twist.angular.z = 0.0

        ##### ② #####
        
        ##############

        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    ##### ③ #####

    ##############

    ##### ④ #####


    ##############


if __name__ == '__main__':
    main()
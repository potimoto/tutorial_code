import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')

        ##### ① #####

        ##############

        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        twist = Twist()

        twist.linear.x = 0.1 #ロボットの並進速度．正の値であれば前進（単位m/s）
        twist.linear.y = 0.0
        twist.linear.z = 0.0

        twist.angular.x = 0.0
        twist.angular.y = 0.0
        twist.angular.z = 0.1 #ロボットの角速度．正の値であれば反時計回り（単位m/s）
          
        ##### ② #####
          
        ##############


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    ##### ③ #####
      
    ##############

    ##### ④ #####
      

    ##############


if __name__ == '__main__':
    main()
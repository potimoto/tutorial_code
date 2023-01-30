import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        ##### ⑤ #####
          
        ##############

        # 未使用変数による警告を防ぐため記述
        self.subscription

    def listener_callback(self, twist):
        self.get_logger().info('linear_x: "%f" angular_z: "%f"' %(twist.linear.x, twist.angular.z))


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    ##### ⑥ #####
      
    ##############

    ##### ⑦ #####
      

    ##############


if __name__ == '__main__':
    main()
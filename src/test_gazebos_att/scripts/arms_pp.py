import rospy,sys
import moveit_commander
from geometry_msgs.msg import PoseStamped, Pose
from test_gazebos_att.srv import Attach, AttachRequest, AttachResponse

class MoveItDemo:
    def __init__(self):
#机械臂a初始化部分
        moveit_commander.roscpp_initialize(sys.argv)

        rospy.init_node("arms_pp")

        arma = moveit_commander.MoveGroupCommander("arma")

        reference_frame = 'base_linka'
        arma.set_pose_reference_frame(reference_frame)
        end_effector_link = arma.get_end_effector_link()                

        arma.allow_replanning(True)

        arma.set_goal_position_tolerance(0.01)
        arma.set_goal_orientation_tolerance(0.01)
        arma.set_max_acceleration_scaling_factor(0.2)
        arma.set_max_velocity_scaling_factor(0.2)

        arma.set_named_target('homea')
        arma.go()
        rospy.sleep(1)

#机械臂a移动到位置
        joint_positions_a1 = [0,-1.57,0,0,0,0]
        arma.set_joint_value_target(joint_positions_a1)
        arma.go()
        rospy.sleep(1)

#机械臂a与物块attach
        attach_srv = rospy.ServiceProxy('/link_attacher_node/attach',Attach)
        attach_srv.wait_for_service()
        req = AttachRequest()
        req.model_name_1 = "cube2"
        req.link_name_1 = "link"
        req.model_name_2 = "arms"
        req.link_name_2 = "link6a"
        attach_srv.call(req)

#携带物块移动到位置
        joint_positions_a2 = [0.00, 0.64, 0.0, 0.0, 0.0 ,0.0]
        arma.set_joint_value_target(joint_positions_a2)
        arma.go()
        rospy.sleep(1)
#机械臂b初始化
        armb = moveit_commander.MoveGroupCommander("armb")

        reference_frame = 'base_linkb'
        armb.set_pose_reference_frame(reference_frame)
        end_effector_link = armb.get_end_effector_link()                

        armb.allow_replanning(True)

        armb.set_goal_position_tolerance(0.01)
        armb.set_goal_orientation_tolerance(0.01)
        armb.set_max_acceleration_scaling_factor(0.2)
        armb.set_max_velocity_scaling_factor(0.2)

        armb.set_named_target('homeb')
        armb.go()
        rospy.sleep(1)

#机械臂b移动到位置
        joint_positions_b1 = [0.10,-0.51,0.26,-0.17,1.27,0.0]
        armb.set_joint_value_target(joint_positions_b1)
        armb.go()
        rospy.sleep(1)

#机械臂a与物块detach
        attach_srv = rospy.ServiceProxy('/link_attacher_node/detach',Attach)
        attach_srv.wait_for_service()
        req = AttachRequest()
        req.model_name_1 = "cube2"
        req.link_name_1 = "link"
        req.model_name_2 = "arms"
        req.link_name_2 = "link6a"
        attach_srv.call(req)
#机械臂b与物块attach
        attach_srv = rospy.ServiceProxy('/link_attacher_node/attach',Attach)
        attach_srv.wait_for_service()
        req = AttachRequest()
        req.model_name_1 = "cube2"
        req.link_name_1 = "link"
        req.model_name_2 = "arms"
        req.link_name_2 = "link6b"
        attach_srv.call(req)        
#机械臂b再次移动
        joint_positions_b2 = [0,1.57,0,0,0,0]
        armb.set_joint_value_target(joint_positions_b2)
        armb.go()
        rospy.sleep(1)

#机械臂b与物块detach
        attach_srv = rospy.ServiceProxy('/link_attacher_node/detach',Attach)
        attach_srv.wait_for_service()
        req = AttachRequest()
        req.model_name_1 = "cube2"
        req.link_name_1 = "link"
        req.model_name_2 = "arms"
        req.link_name_2 = "link6b"

        # 关闭并退出moveit
        moveit_commander.roscpp_shutdown()
        moveit_commander.os._exit(0)        
if __name__ == "__main__":
    MoveItDemo()
====================
ROS Topic Subscriber
====================

-   01_02_ros_topic_subscriber.ipynb
-   Running the cell code
    `Ctrl + Enter`

.. image:: ../images/comm2.webp

.. code-block:: python

    import rospy
    from std_msgs.msg import String

-   Import rospy modules
-   Import String from std_msgs.msg module

.. code-block:: python

    def callback(data):
        rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

-   Create `callback()` function
-   Node id and message data output

.. code-block:: python

    def listener():
        rospy.init_node('listener', anonymous=True)
        rospy.Subscriber("chatter", String, callback)
        rospy.spin()

-   listener 함수 생성
-   listener Node 생성
-   chatter Topic의 Message를 Subscribe
-   Subscriber Callback 처리

.. code-block:: python

    listener()

-   Run the listener function

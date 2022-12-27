=============
Path Planning
=============

What is Path Planning? 
----------------------

| Once the terrain is mapped and the robot knows where it is, **a target and an instruction on where to go** is given to the robot. This process is called path planning.


Move_base
---------

| In path planning, the components and nodes provided by the ROS package itself are called Move_base. The most important point of Move_base is **to move from the current position to the target position**.
|
| Essentially, Move_base is an action type where it receives a topic, performs an action suitable for that topic, and sends the topic again.

.. image:: images/path_planning.svg


.. toctree::
    :hidden:

    path_planning/global_cost
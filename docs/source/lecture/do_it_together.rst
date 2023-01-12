Image Recognition using Camera
===============================


ZetaBot is equipped with Raspberry Pi camera located on the front panel.
Using this camera we can classify real life object using either GoogleNet, or AlexNet networks. 

Our image recognition model can classify up to 1000 images, the list of the classifiable images are:
`<https://github.com/dusty-nv/jetson-inference/blob/master/data/networks/ilsvrc12_synset_words.txt>`_


Let us build a python program as a team for image recognition with camera. 


Writing Python Program as a Team
---------------------------------

Create a new python file in the Jupyter Notebook Environment:

-   Press the blue plus button on the top left corner of the web.

    .. thumbnail:: /_images/ai_training/add_plus.png

-   Create a new python file by pressing the ``Python File`` button

    .. thumbnail:: /_images/ai_training/pick_python.png


-   On the new python file, import the libraries necessary. For our Image Recognition task, we need to import the 
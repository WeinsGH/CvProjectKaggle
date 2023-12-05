# CvProjectKaggle

This work for [Kaggle competition](https://www.kaggle.com/datasets/davidbroberts/brain-tumor-object-detection-datasets)

# Mission

The Kaggle dataset contains 75/310 test/train labled images with positive/negative brain tumors. The task: train a YOLO-model to detect brain tumors with the highest possible accuracy.

![dataset-cover](https://github.com/WeinsGH/CvProjectKaggle/assets/109025285/0b997172-ee7e-4f20-b05f-f773691f7c2b)

# Preprocessing

We were dealing with labled images, but there are few of them to train the model with the best metrics. We have added augmentations used Roboflow.

Added:

![012](https://github.com/WeinsGH/CvProjectKaggle/assets/109025285/4c41232e-7033-463a-b9c0-2c0e83d2dcf1)

# Model

We used YOLO-v5m model as compromise between loss and learning-speed. You must understand the responsibility of the task, if you are planning a release, achieve greater accuracy - collect more data for training, choose heavier models.

# Results and metrics

Model trained by 160 epochs. We used meanAveragePrecision as the main metric. The best result: 0.896 on 162 epoch.

![013](https://github.com/WeinsGH/CvProjectKaggle/assets/109025285/9439e76c-9201-4d86-a653-9184ebb039ff)

![014](https://github.com/WeinsGH/CvProjectKaggle/assets/109025285/826d6c8a-491d-4723-bd4c-745654df2e35)

![016](https://github.com/WeinsGH/CvProjectKaggle/assets/109025285/d62c549e-ed56-4747-b17a-cb7e5d452918)

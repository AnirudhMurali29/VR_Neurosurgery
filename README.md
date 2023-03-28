# VR Training module for Robotic surgery skill acquisition using Kuka IIWA and 3D slicer

This repository contains my Dual Degree Project work as part of my IDDD (Inter-Disciplinary Dual Degree) Programme in IIT Madras, India. 

Objectives:

● Achieve a general setup for the Virtual Reality Training module for minimally invasive
neurosurgery on co-dependent platforms.

● Conduct full-fledged immersive experiments on Human subject

● Validate comparative human acquired registration proficiency and improvements on a
VR platform compared to a 2D medium.

Method:

● Utilize 3D slicer for brain scan data analysis, fiducial registration, and surgery planning

● Cross-platform communication between Unity and 3D slicer.

● KUKA IIWA characterization and implementation of kinematics on a simulation platform.

● A Surgery environment setup and VR stream for immersive usage.

● Experimentation and validation of Robot registration on VR platform by human subjects.

**Unity:**

An overview of the Unity Environment:
![image](https://user-images.githubusercontent.com/87588483/228350300-1985916d-c5f7-4066-af87-655b8cd2fb5a.png)

The skull viewed through iVRy, using an android phone as a virtual VR Headset:
![image](https://user-images.githubusercontent.com/87588483/228350502-3869a6d0-019c-4d61-81a9-18e05c254e12.png)

A view of the tool tip moving according to joystick commands, to register the points marked on the skull:

![image](https://user-images.githubusercontent.com/87588483/228356338-da597053-51ae-45c7-b40d-2bd70df0ce6f.png)

The UI:

![image](https://user-images.githubusercontent.com/87588483/228350628-984fbf99-a6cf-4aea-842d-259d50e83e83.png)

![image](https://user-images.githubusercontent.com/87588483/228350704-ebb94710-16b2-4c1c-95ff-840a21ab6602.png)

While the current setup of our project is is Unity, in the future we'd like to completely move away from Unity and set up our robot entirely using only ROS and 3D Slicer. 

**Slicer:**

Overview of the Slicer Enviornment

![WhatsApp Image 2023-03-23 at 1 24 55 AM](https://user-images.githubusercontent.com/87588483/228369753-7b6a575f-1fa9-4413-92ca-c6cf2ce670b2.jpeg)

## Setting up Slicer:
1) Download Slicer 5.0.3 from  https://slicer-packages.kitware.com/#collection/5f4474d0e1d8c75dfc70547e/folder/62cc513eaa08d161a31c1372
2) Our Slicer Module is still in development and once its completed, will be available to download via the Extensions Manager Wizard. Till then, you can open the "Python Interactor" Window and paste the code from 'final.py' into the window.


## Setting up ROS:
As we wish to move away from Unity and to using only ROS and SLicer, we need to set up ROS and Link it to Slicer. 
We have tried using ROS2 on WIndows and on Ubuntu but due to compatibility and various other issues we decided to use ROS Noetic on Ubuntu 20.04
If you do not have the required operating system you can set up a virtual machine with Oracle VM and install Ubuntu 20.04 there. Plenty of installation tutorials should be easily available for the same.
Once Ubuntu is up and running, follow the following guide: http://wiki.ros.org/noetic/Installation/Ubuntu , to install ROS Noetic.

Once ROS has been installed, follow the following guide: https://github.com/openigtlink/ROS-IGTL-Bridge , to set up the ROS IGTLink Bridge between ROS and Slicer.

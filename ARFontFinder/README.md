# ARFontFinder
The AR application to decode [AR Fonts](../tree/master/fonts).

# Supported Platform
* Android > 4.0

# Requirements
* [OpenCV4Android](http://docs.opencv.org/doc/tutorials/introduction/android_binary_package/O4A_SDK.html)
* [ArUco Android](https://code.google.com/p/aruco-android/)

# Install
## Prepare
You'll need to setup Eclipse or Android studio before install. And Go to [OpenCV download page on SourceForge](http://sourceforge.net/projects/opencvlibrary/files/opencv-android/) and download sdk archive. And checkout [ArUco-Android library from SourceForge](https://code.google.com/p/aruco-android/source/checkout) and import Aruco and min3d-rotation project as Android library project.

## Install ARFontFinder
	git clone https://github.com/mitans02/ohd2.git
Import **ARFontFinder** directory as Android project. 

And then add ArUco and min3d-rotation library to ARFontFinder's android libary path. (If you use eclipse, you can find menu from right click of ARFontFinder project > properties > Android > Library.) 
To build with OpenCV, copy armeabi/armeabi-v7a/x86 directory from OpenCV sdk native libs directory (sdk/native/libs) to ARFontFinder project's libs directory. 

# Getting Started
1. Install ARFontFinder application to device.
1. Launch application.
1. Look at AR Font through application.

# Known Issues and Troubleshooting
# License
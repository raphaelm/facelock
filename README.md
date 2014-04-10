This is how I lock my laptop screen whenever I'm around security people.
It shows the current image of the webcam and marks detected faces by anyone,
emulating a face-recognition lockscreen (which it is not, it is unlocked with
a password). When someone is staring into the webcam longer than X, the script
takes a photo.

This is a very dirty hack. The `facelock` shell script does a bunch things:
* Startup a python script which displays the webcam image and draws a red
  border around faces.
* Ask the window manager (for me, with `i3-msg`) to make the window fullscreen
* Start a transparent lockscreen (`alock`) in front of it.
* As soon as `alock` terminates (screen is unlocked), the python script is killed

To run it on your system, you might need to:
* Adjust some variables in the first lines of the python script
* Adjust the fullscreen mechanism to your window manager
* Replace the lockscreen, I tried `alock` and `xtrlock`


Dependencies
============
* alock (you can replace it by xtrlock)
* opencv with Python bindings
* i3

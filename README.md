# Flappy-Bird
creating flappy bird using pygame.
game is simple we have bird as a player and the score increases. If the bird collide with pipe ,touch the ground and move outside of window game restarts.
first I created the screen which is 288x 512.
than added images of bird ,background ,ground ,pipes.
after that I define bird and gave bird movement(jump).
added another ground and attached it with 1st ground so that when it moves right to left it will look like its going forever.
create a create_pipe function which generate random pipes and also created a move_pipe function to make pipe move from left to right.
creted a function for colllison to check if bird collided with pipes,ground and move out of window.
created a bird animation fuction used 3 bird images to make it look like bird is flapping its wings at 200ms.
than in the end added score and high to game. 
fixed few bugs like blackbox in the image can be solved eassily by just removing convert() in image load method and changing it to convert_alpha()
and added by name.

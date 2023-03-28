# TASK_3_Droame
problem statement:
assume a situation where multiple drones are flying in 2 D space autonomosly . it will create a lot of  mess if there is no central software to guide them the path they have to follow to reach their destination .
you can assume this 2D plane to be a M * N  grid 
your task is to design an algorithm which solves the above problem and gives each drones and a list of drones with their starting position , end position , time at which they will start.
example input : 
[[x11 , y11, x12, y12 , t1] , [x21, y21, x22, y22, t2],........[xn1, yn1, xn2, yn2, tn]]
this input tells us thatv there will be a drone that will appear at point (x11, y11) at time t1 and wants to reach its destination pount (x12, y12) 
similiarly , there are certain other drones which will apperar at their starting position at their corresponding time , and their target destination .
your output should be the path for each drone which can be followed by the drone  to reach its destination .
A path is nothing but just a sequence of positionswhich are adjacent to each other . you can assume that each drone can move from its position to its adjacent position in 1 second .
you can assume 8 adjacent i.e all 8 cells around  a particular cell are adjacent to it implying that the drone can move in all directions .
if you wish to go for 4 adjacency i.e assuming that the drone can move only in 4 directions forward , backward , left and right , then this can also be considered .
the algorithm should be designed in such a way that there occurs no collision between the drones should possibly reach their destination in minimum time possible .
you can assume that size of each drone is 1*1 unit and total grid size to be 20*20 units .
apart from all this, you are free to assume some suitable and valid assumptions.
you are expected to provide the following :
you have to code this algorithm down in any language you are comfortable with .
also, you have to simulate the rdesult by displaying how multiplr drones will travel to reach their target destination .
you have to also think of a method to enter/give dynamic inputs easily .
a document that explains the approach taken any libraries or frameworks used, and how to run the application. 

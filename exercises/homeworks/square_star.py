# *  *  *  *
# *        *
# *        *
# *  *  *  *

for i in range(4):
    for j in range(4):
        if i == 0 or i == 3 or j == 0 or j == 3 :
            print("*", end="  ")
        elif i == 1 or i == 4 or j == 1 or j == 2: 
            print(" ", end="  ")
    print()

# for i in range(4):
#     for j in range(4):
#         if i == 0 or i == 3 or j == 0 or j == 2 or j == 4 or j == 6 :
#             print("*", end=" ")
#         elif i == 1 or i == 4 or j == 1 or j == 2: 
#             print(" ", end=" ")
#     print()

# Trace
# outer loop ==> 0 (*)
        # inner loop ==> 0 (*)
        # inner loop ==> 1 ()
        # inner loop ==> 2 (*)
        # inner loop ==> 3 ()
        # inner loop ==> 4 (*)
        # inner loop ==> 5 ()
        # inner loop ==> 6 (*)
        

# outer loop ==> 1 ()
        # inner loop ==> 0 (*)
        # inner loop ==> 1 ()
        # inner loop ==> 2 ()
        # inner loop ==> 3 ()
        # inner loop ==> 4 ()
        # inner loop ==> 5 ()
        # inner loop ==> 6 (*)
        

# outer loop ==> 2
        # inner loop ==> 0 (*)
        # inner loop ==> 1 ()
        # inner loop ==> 2 ()
        # inner loop ==> 3 ()
        # inner loop ==> 4 ()
        # inner loop ==> 5 ()
        # inner loop ==> 6 (*)
        
# outer loop ==> 3
        # inner loop ==> 0 (*)
        # inner loop ==> 1 ()
        # inner loop ==> 2 (*)
        # inner loop ==> 3 ()
        # inner loop ==> 4 (*)
        # inner loop ==> 5 ()
        # inner loop ==> 6 (*)
        
    
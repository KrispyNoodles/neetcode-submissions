from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        # createsstack
        stack_stu = deque(students)
        stack_stand = deque(sandwiches)

        rotations = 0
        
        # possible that the students in the stack do not want the sandwiches anymore
        while True:
            
            pop_stu = stack_stu.popleft()
            pop_sand = stack_stand[0]

            # if there is a student and there is a sanwich
            # they are both removed from the queue
            # if both is circular take and leave
            if pop_stu == 1 and pop_sand==1:

                # reset when a student eats the sandwich
                rotations=0

                # when they take and leave the sandwich moves and the students leave as well
                stack_stand.popleft()
            
            # if pop_stu is 0 then take and go
            # if both is square take and leave
            elif pop_stu == 0 and pop_sand == 0:
                # reset when a student eats the sandwich
                rotations=0
                stack_stand.popleft()

            else:
                # else append them back in the queue
                stack_stu.append(pop_stu)
                rotations+=1

            # if either is empty then reutrn
            if len(stack_stu)==0 or len(stack_stand)==0:
                break

            # if all students rotated once before already
            if rotations == len(stack_stu):
                break
            
        return len(stack_stu)
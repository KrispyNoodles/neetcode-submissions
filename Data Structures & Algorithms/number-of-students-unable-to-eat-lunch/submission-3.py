class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        answer = len(students)

        dic = Counter(students)

        # go through all the sandiwches
        for s in sandwiches:

            # if more than 0 can minus
            if dic[s]>0:
                dic[s]-=1
                answer-=1
            else:
                break

        return answer
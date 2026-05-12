class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjList = {}

        # creating a dict
        for i in range(numCourses):
            adjList[i]=[]

        # create an adjList from the prerequisites
        for start, dstn in prerequisites:

            # then add the dstn to the start
            adjList[start].append(dstn)
        
        visitSet = set()

        # base cases
        # you dont need take any course
        if adjList == {}:
            return True


        def dfs(course):

            # if we visit the node again
            if course in visitSet:
                return False

            # if pre-requisite have nothing in the array then we can return True
            if adjList[course] == []:
                return True

            # now we visit it
            visitSet.add(course)

            # looking through its neighbours
            for neighbours in adjList[course]:
                
                # if false already above then can just immediately skip
                if dfs(neighbours) == False:
                    return False

            # backtrack?
            visitSet.remove(course)
            # reassign, so when it reaches, there again we alreayd know that it is accessible
            adjList[course] = []
            return True

        for course in range(numCourses):
            if dfs(course)==False:
                return False

        # runs till the end
        return True
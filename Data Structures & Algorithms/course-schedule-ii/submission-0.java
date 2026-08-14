class Solution {
  
    private Map<Integer, List<Integer>> adjList;
    private Set<Integer> completedCourse;
    private Set<Integer> visited;
    private int[]order ;
    private int indx = 0;
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        adjList = new HashMap<>();
        completedCourse = new HashSet<>();
        visited = new HashSet<>();
        order = new int[numCourses];
        
        for (int i = 0; i < numCourses; i++) {
            adjList.put(i, new ArrayList<>());
        }


        for (int[] p : prerequisites) {
            int a = p[0];
            int b = p[1];
            adjList.get(a).add(b);
        }

        
        for (int i = 0; i < numCourses; i++) {
            if (!dfs(i)) {
                return new int[0]; // Cycle detected
            }
        }
        return order;
    }



     private boolean dfs(int course) {
        if (visited.contains(course)) {
            return false;
        }  
        if (completedCourse.contains(course)) {
            return true;
        }

        visited.add(course);
        
        for (int crs : adjList.get(course)) {
            if (!dfs(crs)) {
                return false;
            }
        }
        
        visited.remove(course);
        order[indx++] = course;
        completedCourse.add(course);

        return true;
    }

}
class Solution {
    private static int EMPTY = 0;
    private static int FRESH = 1;
    private static int ROTTEN = 2;

    private static int[][] DIRECTIONS = {{1,0}, {-1, 0}, {0,1}, {0,-1}};

    public int orangesRotting(int[][] grid) {

    int rows = grid.length;
    int cols = grid[0].length;
    Queue<int[]> queue = new ArrayDeque<>();


    for(int row = 0; row< rows; row++){

        for(int col = 0; col< cols; col++){

            if(grid[row][col]==ROTTEN){
                queue.offer(new int[]{row,col});
            }
        }
    }

    int rottenCountPerMin = queue.size();
    int minute = 0;

    while(!queue.isEmpty()){
        
        int[] current = queue.poll();
        rottenCountPerMin--;
        int row = current[0];
        int col = current[1];

        for(int[] dir : DIRECTIONS){
            
            int nextRow = row+dir[0];
            int nextCol = col+dir[1];
            if(isFresh(rows, cols, nextRow, nextCol, grid)){
                grid[nextRow][nextCol] = ROTTEN;
                queue.offer( new int[]{nextRow, nextCol});
            }
        }

        if (rottenCountPerMin == 0){
            rottenCountPerMin = queue.size();
                if (!queue.isEmpty()) { 
                    minute += 1;
                }            
            
        }

    }

    for(int row = 0; row< rows; row++){

        for(int col = 0; col< cols; col++){

            if(grid[row][col]==FRESH){
                return -1;
            }
        }
    }    

    return minute;

    }
    private boolean isFresh(int rows, int cols , int row , int col, int[][] grid){

        if(row<0 || col < 0 || row>= rows || col>=cols || grid[row][col]!=FRESH ){
            return false;
        }
        return true;
    }

}

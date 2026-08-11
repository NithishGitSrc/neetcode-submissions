class Solution {
    
    private static int GATE = 0;
    private static int EMPTY_ROOM = Integer.MAX_VALUE;

    private static int[][] DIRECTIONS = {{-1,0},{1,0},{0,1},{0,-1}};

    public void islandsAndTreasure(int[][] grid) {

        Queue<int[]> queue = new ArrayDeque<>();
        int rows = grid.length, cols = grid[0].length;


        for(int i = 0; i < rows; i++){

            for(int j = 0 ; j < cols; j++){

                if(grid[i][j]==0){
                    queue.offer(new int[]{i,j});
                }

            }
        }

        while(!queue.isEmpty()){
            int[] coordinates =  queue.poll();
            int row = coordinates[0], col = coordinates[1];

            for( int[] dir : DIRECTIONS){
                int nextRow = row+dir[0];
                int nextCol = col+dir[1];

                if(isValidRoom(rows, cols, nextRow, nextCol, grid)){
                    grid[nextRow][nextCol] = grid[row][col] + 1;
                    queue.offer(new int[]{nextRow, nextCol});
                }

            }

        }

    }
    private boolean isValidRoom(int rows, int cols , int r, int c, int[][] grid){
        if( r < 0  || c < 0 || r >= rows || c >= cols || grid[r][c]!=2147483647 ){
            return false;
        }
        return grid[r][c]==EMPTY_ROOM;
    }
}
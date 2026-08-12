
class Point{

    int r, c;
    Point(int r , int c){
        this.r = r;
        this.c = c;
    }
    @Override
    public boolean equals(Object o ){
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Point point = (Point) o;
        return r==point.r && c==point.c;
    }

    @Override
    public int hashCode() {
        return Objects.hash(r, c); 
    }    

}
class Solution {

    private Set<Point> nonCapturable = new HashSet<>(); 
    private static int[][] DIRECTIONS = {{1,0},{-1,0}, {0,1}, {0,-1}};


    public void solve(char[][] board) {
        

        int ROWS = board.length;
        int COLS = board[0].length;
        
        for(int row = 0 ; row < ROWS; row++){
            dfs(row, 0, ROWS, COLS , board);
            dfs(row, COLS-1,  ROWS, COLS, board);
        }

        for(int col = 0 ; col < COLS; col++){
            dfs(0,col,ROWS,COLS, board);
            dfs(ROWS-1,col,ROWS,COLS, board);
        }

        for(int row = 0 ; row < ROWS; row++){
            for(int col = 0 ; col < COLS; col++){
                if(board[row][col]=='O' && !nonCapturable.contains(new Point(row, col))){
                    board[row][col] = 'X';
                }
            }
        }

    }

    public void dfs(int row, int col, int rows, int cols, char[][]board){

        if(row < 0 || col < 0 || row >= rows ||
            col >= cols || board[row][col]!='O' ||
            nonCapturable.contains(new Point(row,col))){
            return;
        }
        
        nonCapturable.add(new Point(row, col));

        for(int[] dir : DIRECTIONS){

            int nxtRow = row + dir[0];
            int nxtCol = col + dir[1];

            dfs(nxtRow, nxtCol , rows, cols, board);
        }

        return;

    }
}

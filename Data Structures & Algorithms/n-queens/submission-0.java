class Solution {
    public List<List<String>> solveNQueens(int n) {
        Set<Integer> col = new HashSet<>();
        Set<Integer> posDiag = new HashSet<>();
        Set<Integer> negDiag = new HashSet<>();
        
        List<List<String>> res = new ArrayList<>();
        char[][] board = new char[n][n];
        for(char[] row: board){
            Arrays.fill(row, '.');
        }
        backtrack(0, n, col, posDiag, negDiag, board, res);
        return res;
    }
    private void backtrack(int r, int n, Set<Integer> col, Set<Integer> posDiag, Set<Integer> negDiag, char[][] board, List<List<String>> res){
        if(r == n){
            List<String> copy = new ArrayList<>();
            for(char[] row: board){
                copy.add(new String(row));
            }
            res.add(copy);
            return;
        }
        for(int c=0; c < n; c++){
            if(col.contains(c) || posDiag.contains(c + r) || negDiag.contains(r -c)){
                continue;
            }
            col.add(c);
            posDiag.add(r + c);
            negDiag.add(r - c);
            board[r][c] = 'Q';
            backtrack(r + 1, n, col, posDiag, negDiag, board, res);
            board[r][c] = '.';
            negDiag.remove(r - c);
            posDiag.remove(r + c);
            col.remove(c);
        }
        return;
    }
}

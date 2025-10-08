function solution(board, moves) {
    const bucket = [];
    let answer = 0;
    const lanes = [...new Array(board.length)].map(() => []);
    for (let i = board.length - 1; i >= 0; i--) {
        for (let j = 0; j < board[0].length; j++) {
            if (board[i][j]) {
                lanes[j].push(board[i][j]);
            }
        }
    }
    for (const m of moves) {
        if (lanes[m - 1].length > 0) {
            const doll = lanes[m - 1].pop();
            if (bucket.length > 0 && doll === bucket[bucket.length - 1]) {
                bucket.pop();
                answer += 2;
            } else {
                bucket.push(doll);
            }
        }
    }
    return answer;
}
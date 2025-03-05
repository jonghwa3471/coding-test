const solution = (board) => {
    const boardSize = board.length * board.length;
    let result = 0;
    let targetX = 0;
    let target = [];
    for (let i = 0; i < board.length; i++) {
        if (board[i].includes(1)) {
            targetX = i;
            board[i].forEach((value, index) => {
                if (value === 1) target.push([targetX, index]);
            })
        }
    }
    target.forEach((value) => {
        let target = []
        for (let i = value[1] - 1; i <= value[1] + 1; i++) {
            target.push([value[0] - 1, i]);
            target.push([value[0], i]);
            target.push([value[0] + 1, i]);
            target = target.filter(([x, y]) => x >= 0 && y >= 0 && x < board.length && y < board.length);
        }
        target.forEach((value) => board[value[0]][value[1]] = 1);
    })
        board.forEach((value) => {
            value.forEach((bomb) => {
                if (bomb === 1) result += 1;
            })
        })
    return boardSize - result;
}
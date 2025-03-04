const solution = (keyinput, board) => {
    let result = [0, 0];
    const maxBoard = [Math.abs(Math.floor(board[0] / 2)), Math.abs(Math.floor(board[1] / 2))];
    keyinput.forEach((key) => {
        if (key === "up") {
            result[1] += 1;
            if (Math.abs(result[1]) > maxBoard[1]) result[1] += -1;
        }
        if (key === "down") {
            result[1] += -1;
            if (Math.abs(result[1]) > maxBoard[1]) result[1] += 1;
         }
        if (key === "left") {
            result[0] += -1;
            if (Math.abs(result[0]) > maxBoard[0]) result[0] += 1;
        }
        if (key === "right") {
            result[0] += 1;
            if (Math.abs(result[0]) > maxBoard[0]) result[0] += -1;
        }
    })
    return result;
}
function solution(n , k, cmd) {
    const deleted = [];
    const up = [...new Array(n + 2)].map((_, i) => i - 1);
    const down = [...new Array(n + 1)].map((_, i) => i + 1);
    
    k += 1;
    
    for (const item of cmd) {
        if (item[0] === "C") {
            deleted.push(k)
            down[up[k]] = down[k];
            up[down[k]] = up[k];
            k = n < down[k] ? up[k] : down[k];
        } else if (item[0] === "Z") {
            const restore = deleted.pop();
            down[up[restore]] = restore;
            up[down[restore]] = restore;
        } else {
            const [move, times] = item.split(" ");
            if (move === "D") {
              for (let i = 0; i < times; i++) {
                  k = down[k];
              }  
            } else {
                for (let i = 0; i < times; i++) {
                    k = up[k];
                }
            }
        }
    }
    const answer = new Array(n).fill("O");
    for (const i of deleted) {
        answer[i - 1] = "X";
    }
    return answer.join("");
}
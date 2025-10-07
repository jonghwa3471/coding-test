function solution(s) {
    const stack = [];
    for (const c of s) {
        if (stack.length > 0) {
            const top = stack[stack.length - 1];
            if (top === c) {
                stack.pop();
            } else {
                stack.push(c);
            }
        } else {
            stack.push(c);
        }
    }
    return stack.length === 0 ? 1 : 0;
}
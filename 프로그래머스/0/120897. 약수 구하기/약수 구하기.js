const solution = (n) => {
    if(n === 1) return [1];
    let result = [];
    for(let i = 1; i <= Math.sqrt(n); i++) {
        if (n % i === 0) {
            result.push(i, n / i);
            if (Math.sqrt(n) === i) result.pop();
        }
    }
    result = result.sort((a, b) => a - b);
    console.log(result);
    return result;
}
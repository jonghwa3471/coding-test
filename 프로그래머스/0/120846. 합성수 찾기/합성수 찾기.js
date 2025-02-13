const calculator = (number) => {
    let count = 0;
    for (let i = 1; i * i <= number; i++) {
        if(number % i === 0) {
            count++;
            if (i !== number / i) count++;
        }
    }
    return count;
}

const solution = (n) => {
    let result = 0;
    for (let i = 1; i <= n; i++) {
        if (calculator(i) >= 3) result++;
    }
    return result;
}
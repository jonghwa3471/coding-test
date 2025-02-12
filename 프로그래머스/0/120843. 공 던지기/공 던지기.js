const solution = (numbers, k) => {
    let result = 0;
    for (let i = 0; i < k; i++) {
        result = numbers[2 * i % numbers.length];
    }
    return result;
}
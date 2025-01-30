const solution = (n) => {
    const squareRoot = n ** 0.5;
    const result = n % squareRoot === 0 ? 1 : 2;
    return result;
}
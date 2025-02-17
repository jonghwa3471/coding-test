const solution = (array, n) => {
    array.sort((a, b) => a - b);
    let min = Infinity;
    let result;
    array.forEach((value) => {
        const abs = Math.abs(n - value);
        if (abs < min) {
            min = abs;
            result = value;
        }
    })
    return result;
}
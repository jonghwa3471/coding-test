const solution = (numbers) => {
    const sorted = [...numbers].sort((a, b) => b - a);
    const max = sorted[0];
    const second = sorted[1];
    let third = 0;
    const minus = sorted.filter((number) => number < 0);
    const result = max * second;
    
    if (minus.length > 1) {
        third = minus[0] * minus[1];
        if (third > result) return third;
    }
    return result;
}
const solution = (sides) => {
    const sorted = [...sides].sort((a, b) => a - b);
    const max = sorted[1];
    const min = sorted[0];
    const numbers = Array(max).fill(1).map((value, index) => value + index);
    const maxBase = numbers.filter((number) => number + min > max);
    const anotherBase = [];
    
    for (let i = max + 1; i < min + max; i++) {
        anotherBase.push(i);
    }
    return maxBase.length + anotherBase.length;
}
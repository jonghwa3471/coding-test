const solution = (n) => {
    let array = [];
    for (let i = 1; i <= n; i++) {
        array.push(i);
    }
    const evenArray = array.filter((number) => number % 2 !== 0);
    return evenArray;
}
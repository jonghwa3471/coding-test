const solution = (n) => {
    const numbers = Array(n * 2).fill(1).map((number, index) => number + index);
    const filtered = numbers.filter((number) => number % 3 !== 0);
    console.log(filtered)
    const notAllowed3 = filtered.filter((number) => !String(number).includes("3"));
    const result = notAllowed3[n - 1];
    return result;
}
const solution = (n) => {
    const stringArray = Array.from(String(n));
    const result = stringArray.reduce((acc, cur) => Number(acc) + Number(cur), 0);
    return result;
}
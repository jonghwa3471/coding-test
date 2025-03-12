const solution = (numlist, n) => {
    let result = [];
    numlist.sort((a, b) => b - a);
    numlist.sort((a, b) => Math.abs(a - n) - Math.abs(b - n));
    return numlist;
}
const solution = (n, numlist) => {
    const filtered = numlist.filter((value) => value % n === 0);
    return filtered;
}
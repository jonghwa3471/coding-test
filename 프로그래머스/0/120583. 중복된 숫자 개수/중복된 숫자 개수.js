const solution = (array, n) => {
    let result = [];
    result = array.filter((value) => value === n);
    return result.length;
}
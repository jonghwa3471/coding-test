const solution = (num, k) => {
    let result = 0;
    const numsArray = String(num).split("");
    if (numsArray.includes(String(k))) {
        result = numsArray.indexOf(String(k)) + 1;
    } else {
        return -1;
    }
    return result;
}
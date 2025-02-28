const solution = (my_str, n) => {
    let result = [];
    const offset = n;
    const length = Math.ceil(my_str.length / offset);
    const strArray = my_str.split("");
    for (let i = 0; i < length; i++) {
        const piece = strArray.slice(i * offset, offset + i * offset);
        result.push(piece.join(""));
    }
    return result;
}
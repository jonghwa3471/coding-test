const solution = (cipher, code) => {
    let result = [];
    const array = cipher.split("");
    for (let i = code; i <= cipher.length; i += code) {
        result.push(array[i - 1]);
    }
    return result.join("");
}
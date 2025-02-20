const solution = (s) => {
    let result = [];
    const string = s;
    const stringArray = string.split("").sort();
    stringArray.forEach((value) => {
        const filtered = stringArray.filter((string) => string === value);
        if (filtered.length === 1) {
            result.push(value);
        }
    })
    return result.join("");
}
function solution(my_string, n) {
    const stringArray = Array.from(my_string, (string) => {
        return string.repeat(n);
    })
    return stringArray.join("");
}
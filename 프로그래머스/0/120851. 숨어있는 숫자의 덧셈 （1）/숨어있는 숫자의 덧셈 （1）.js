const solution = (my_string) => {
    const numbers = my_string.split("").filter((value) => !isNaN(Number(value))).map((value) => Number(value));
    const result = numbers.reduce((acc, cur) => acc + cur, 0);
    return result;
}
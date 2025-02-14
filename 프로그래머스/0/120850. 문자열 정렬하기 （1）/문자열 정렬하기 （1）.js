const solution = (my_string) => {
    const numbers = Array.from(my_string).filter((string) => !isNaN(Number(string)))
    const result = numbers.map((value) => Number(value)).sort((a, b) => a - b);
    return result;
}
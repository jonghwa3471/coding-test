const solution = (numbers) => {
    const sortNumbers = numbers.sort((a, b)=> b - a);
    const result = sortNumbers[0] * sortNumbers[1];
    return result;
}
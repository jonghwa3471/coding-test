const solution = (n) => {
    let numbers = [];
    let i = 1;
    let k = 0;
    let result = 0;
    while (i <= n ) {
        numbers.push(i);
        i++;
    }
    const evenNumbers = numbers.filter((n) => n % 2 === 0);
    while ( k < evenNumbers.length) {
        result += evenNumbers[k];
        k++;
    }
    return result
}
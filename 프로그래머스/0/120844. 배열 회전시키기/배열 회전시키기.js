const solution = (numbers, direction) => {
    if (direction === "right") {
        const last = numbers[numbers.length - 1];
        numbers.pop();
        numbers.unshift(last);
        return numbers;
    }
    if (direction === "left") {
        const first = numbers[0];
        numbers.shift();
        numbers.push(first);
        return numbers;
    }
}
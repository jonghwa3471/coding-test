const solution = (numbers) => {
    const numberArray = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
    let newArray = numbers;
    numberArray.forEach((number, index) => {
        newArray = newArray.replaceAll(number, index);
    })
    return Number(newArray);
}
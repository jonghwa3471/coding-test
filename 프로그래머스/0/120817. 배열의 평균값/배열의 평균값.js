const solution = (numbers) => {
    let result = 0;
    const newArray = numbers.map((number)=> {
        result += number;
    })
    result = result / newArray.length;
    return result
}
const solution = (array) => {
    const newArray = [...array];
    const orderedArray = newArray.sort((a, b) => a - b);
    const biggest = orderedArray.at(-1);
    const index = array.indexOf(biggest);
    return [biggest, index];
}
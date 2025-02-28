const solution = (array) => {
    let counter = 0;
    array.forEach((value) => {
        const valueArray = String(value).split("");
        valueArray.forEach((stringNumber) => {
            if (stringNumber.includes("7")) counter++;
        })
    })
    return counter
}
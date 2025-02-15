const solution = (s) => {
    let result = 0;
    const stringArray = s.split(" ");
    stringArray.forEach((value, index) => {
        if(value === "Z") result -= Number(stringArray[index - 1]);
        else result += Number(value);
    })
    return result;
}
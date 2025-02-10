const solution = (emergency) => {
    const sortArray = [...emergency].sort((a, b) => b - a);
    let obj = {};
    sortArray.forEach((value, index) => {
        obj[value] = index + 1;
    })
    console.log(obj);
    const result = emergency.map((value) => obj[value]);
    return result;
}
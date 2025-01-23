const solution = (s1, s2) => {
    const result = [];
    s1.forEach((item1)=> {
        const newArray = s2.filter((item2) => item1 === item2)
        result.push(...newArray);
    })
    return result.length;
}
const solution = (rsp) => {
    let result = ""
    const rspArray = Array.from(rsp);
    rspArray.forEach((value) => {
        if (value === "2") result += "0";
        if (value === "0") result += "5";
        if (value === "5") result += "2";
    })
    return result
}
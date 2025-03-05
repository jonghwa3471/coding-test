const solution = (my_string) => {
    const regExp = /[A-Za-z]/g;
    const newStrings = my_string.replaceAll(regExp, " ").split("");
    const join = newStrings.join("").trim();
    const newArray = join.split(" ").filter((value) => value !== "");
    const result = newArray.reduce((acc, cur) => acc + Number(cur), 0);
    return result;
}
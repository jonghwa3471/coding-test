const solution = (my_string, num1, num2) => {
    const stringArray = my_string.split("");
    const first = stringArray[num1];
    const second = stringArray[num2];
    stringArray[num1] = second;
    stringArray[num2] = first;
    return stringArray.join("");
}
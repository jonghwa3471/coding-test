const solution = (my_string) => {
    const reverseArray = my_string.split('').reverse();
    const result = reverseArray.join("");
    return result;
}
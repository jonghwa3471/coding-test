const solution = (my_string) => {
    const onlyOnce = new Set(my_string.split(""));
    const result = Array.from(onlyOnce);
    return result.join("");
}
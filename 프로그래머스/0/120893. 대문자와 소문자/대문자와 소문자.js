const solution = (my_string) => {
    let newArray = my_string.split("");
    const mapping = newArray.map((value) => 
        value === value.toUpperCase() ? value.toLowerCase() : value.toUpperCase());
    return mapping.join("");
}
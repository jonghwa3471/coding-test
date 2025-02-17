const solution = (order) => {
    const orderArray = String(order).split("");
    const filtered = orderArray.filter((value) => value === "3" || value === "6" || value === "9");
    const result = filtered.length;
    return result;
}
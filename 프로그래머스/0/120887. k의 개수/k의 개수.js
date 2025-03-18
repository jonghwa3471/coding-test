const solution = (i, j, k) => {
    const array = Array(j - i + 1).fill(i).map((value, index) => value + index);
    const join = array.join("");
    const filtered = join.split("").filter((value) => value === String(k));
    return filtered.length;
}
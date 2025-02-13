const solution = (box, n) => {
    const [x, y, z] = box.map((value) => Math.floor(value / n));
    return x * y * z;
}
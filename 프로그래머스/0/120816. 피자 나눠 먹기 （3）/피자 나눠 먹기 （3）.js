const solution = (slice, n) => {
    let divide = Math.floor(n / slice);
    const pizza = divide * slice >= n ? divide : divide + 1;
    return pizza
}
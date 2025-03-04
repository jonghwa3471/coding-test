const solution = (polynomial) => {
    let otherNumber = 0;
    
    const terms = polynomial.split("+").map(term => term.trim());

    const others = terms.filter(value => !value.includes("x"));
    const xTerms = terms.filter(value => value.includes("x"));
    console.log(xTerms)
    
    if (others.length > 0) {
        otherNumber = others.reduce((a, b) => Number(a) + Number(b), 0);
    }
    
    const xSum = xTerms.map(value => value.trim() === "x" ? "1" : value.split("x")[0].trim()).map(Number).reduce((a, b) => a + b, 0);
    
    let xPart = xSum === 0 ? "" : (xSum === 1 ? "x" : `${xSum}x`);
    let otherPart = otherNumber === 0 ? "" : `${otherNumber}`;
    if (xSum === 0) return `${otherNumber}`;
    return xPart && otherPart ? `${xPart} + ${otherPart}` : xPart || otherPart;
}
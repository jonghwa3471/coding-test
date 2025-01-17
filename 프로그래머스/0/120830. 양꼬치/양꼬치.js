const solution = (n, k) => {
    const freeDrinkAmount = Math.trunc(n / 10);
    const mainMenuPrice = 12000 * n;
    const drinkPrice = 2000 * (k - freeDrinkAmount);
    const totalPrice = mainMenuPrice + drinkPrice;
    return totalPrice
}
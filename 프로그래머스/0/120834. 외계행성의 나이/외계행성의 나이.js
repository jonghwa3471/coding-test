function solution(age) {
    const alphabetArray = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"];
    const parsedArray = String(age).split("").map((number) => alphabetArray[number]);
   return parsedArray.join("");
}
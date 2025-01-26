const solution = (my_string) => {
    const vowel = ["a", "e", "i", "o", "u"];
    const result = Array.from(my_string).filter((string)=> !vowel.includes(string)).join("");
    return result;
}
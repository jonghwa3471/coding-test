const solution = (babbling) => {
    let count = 0;
    const able = ["aya", "ye", "woo", "ma"];
    babbling.forEach((babble) => {
        let changed = babble;
        able.forEach((word) => {
            changed = changed.replaceAll(word, " ");
        })
        if(changed.trim() === "") {
            count++;
        }
    })
    return count;
}
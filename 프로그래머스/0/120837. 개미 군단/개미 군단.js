const solution = (hp) => {
    const knight = Math.trunc(hp / 5);
    const rook = Math.trunc((hp % 5) / 3);
    const pawn = Math.trunc((hp % 5) % 3);
    const result = knight + rook + pawn;
    return result;
}
export const toMMDTitle = (text: string) => {
    const words = text.split(" ").filter(Boolean).map(w => w.trim().toLowerCase());
    const result = [];

    for (let word of words) {
        if (word === "masmedan") {
            result.push("Más Me Dan");
        } else if (["cc", "mmd", "si", "mmdsi", "cf"].includes(word)) {
            result.push(word.toUpperCase());
        } else {
            result.push(word.at(0)?.toUpperCase() + word.slice(1).toLowerCase());
        }
    }

    return result.join(" ");
};

export const toMoney = (money: number) => {
    const fixed = money.toFixed(2);
    const [integer, decimal] = fixed.split(".");
    const fragments = [];

    for (let i = integer.length; i > 0; i -= 3) {
        fragments.unshift(integer.slice(Math.max(0, i - 3), i));
    }

    return `${fragments.join(",")}.${decimal}`;
}
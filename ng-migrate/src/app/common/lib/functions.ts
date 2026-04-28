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
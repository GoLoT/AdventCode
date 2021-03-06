const inpt = 1308;

const cell = (x, y, serial=inpt) => Math.floor(((x + 10) * y + serial) * (x + 10) % 1000 / 100) - 5;

function gridVal (x, y, s=3) {
  let sum = 0;
  for (let dx = 0; dx < s; dx++) {
    for (let dy = 0; dy < s; dy++) {
      sum += cell(x + dx, y + dy);
    }
  }
  return sum;
}

console.time('Time BF');
let [n, max, mx, my, ms] = [0, 0, 0, 0, 0];
for (let s = 1; s <= 300; s++) {
  for (let x = 1; x <= 300 - s + 1; x++) {
    for (let y = 1; y <= 300 - s + 1; y++) {
      n = gridVal(x, y, s);
      if (n > max) {
        [max, mx, my, ms] = [n, x, y, s];
      }
    }
  }
}
console.timeEnd('Time BF');

console.log(`${mx},${my},${ms}`);

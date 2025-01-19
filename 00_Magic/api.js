// fetch(
//   "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
// )
//   .then((response) => response.json())
//   .then((data) => {
//     console.log(`Bitcoin price: $${data.bitcoin.usd}`);
//   })
//   .catch((error) => console.error("Error:", error));
const p1 = new Promise((resolve, reject) => {
  setTimeout(() => reject("P1 Success"), 3000);
});
const p2 = new Promise((resolve, reject) => {
  setTimeout(() => reject("P2 Success"), 1000);
});
const p3 = new Promise((resolve, reject) => {
  setTimeout(() => reject("P3 Success"), 500);
});
Promise.any([p1, p2, p3])
  .then((res) => {
    console.log(res);
  })
  .catch((err) => {
    console.error(err);
    console.log(err.errors[2]);
  });

let name = {
  firstname: "A",
  lastname: "B",
};
let printname = function (home, town) {
  console.log(this.firstname + this.lastname + " from " + home + " " + town);
};

let name2 = {
  firstname: "Jane",
  lastname: "esh",
};

Function.prototype.mybind = function (...args) {
  let obj = this,
    params = args.slice(1);
  return function () {
    obj.apply(args[0], [...params, ...args]);
  };
};
printname.apply(name, ["Jan", "Har"]);
let p = printname.mybind(name, ["Jan", "Har"]);
p();

// let m = function (x, y) {
//   console.log(x * y);
// };
// let m2 = m.bind(this, 2);
// m2(10, 1);

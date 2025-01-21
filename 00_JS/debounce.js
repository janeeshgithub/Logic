let obj = {
  name: "Janeesh",
  city: "Dehra",
  getIntro: function () {
    console.log(this.name + " ");
  },
};
obj.getIntro();
let obj2 = {
  name: "Abc",
};
obj2.__proto__ = obj;
console.log(obj2.city);

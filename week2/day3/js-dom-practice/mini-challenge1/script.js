

const users = [
  { name: "Alice", age: 22 },
  { name: "Bob", age: 30 },
  { name: "Charlie", age: 28 },
];


const adults = users.filter( (user) => user.age >= 23);
console.log(adults.map( adult => adult.name))

const user_name = users.map(user => user.name);
console.log(`all users are ${user_name}`);

const avgAge = users.reduce( (acc , val) => acc + val.age , 0) / users.length;
console.log(`average age of users is ${avgAge.toFixed(2)}`);


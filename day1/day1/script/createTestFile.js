const fs = require('fs');


var data = '';

for(let i=0; i<1000000; i++) {
  data += 'this is some test data that i am using to create a big test fie.\n ';
}

fs.writeFile('testfile.txt' , data , (err) => {
 if(err) {
   console.log('Error wrting to file:' , err);
   return;
 }
});



console.log('file created succesfully');

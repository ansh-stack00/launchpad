const fs = require('fs');
const { performance } = require('perf_hooks');


let performanceData = {
  buffer: {
    executionTime: null,
    memoryUsage: null
  },
  stream: {
    executionTime: null,
    memoryUsage: null
  }
}

// Using Buffer 
const startBuffer = performance.now();
const memoryBeforeBuffer = process.memoryUsage().heapUsed;

fs.readFile('testfile.txt', 'utf8', (err, data) => {
  if (err) throw err;

  const endBuffer = performance.now();
  const memoryAfterBuffer = process.memoryUsage().heapUsed;

  performanceData.buffer.executionTime = (endBuffer - startBuffer).toFixed(3); // ms
  performanceData.buffer.memoryUsage = ((memoryAfterBuffer - memoryBeforeBuffer) / (1024 * 1024)).toFixed(2); // MB
  
  //  using stream 

  const startStream = performance.now();
  const memoryBeforeStream = process.memoryUsage().heapUsed;

  const readStream = fs.createReadStream('testfile.txt', 'utf8');


  let dataStream = '';
  readStream.on('data', chunk => {
    dataStream += chunk;
  });

  readStream.on('end', () => {
    const endStream = performance.now();
    const memoryAfterStream = process.memoryUsage().heapUsed;

    performanceData.stream.executionTime = (endStream - startStream).toFixed(3); // ms
    performanceData.stream.memoryUsage = ((memoryAfterStream - memoryBeforeStream) / (1024 * 1024)).toFixed(2); // MB

    // writing data in json format 

    fs.writeFileSync('/home/anshagrawal/bootcamp-week1/day1/logs/day1-perf.json', JSON.stringify(performanceData, null, 2), 'utf8');
    console.log('Performance data saved to day1-perf.json');
  });

});

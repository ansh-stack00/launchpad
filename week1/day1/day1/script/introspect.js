const os = require('os');
const path = require('path');
const systemInfo = {
  OS: os.type() + ' ' + os.release(),
  Architecture: os.arch(),
  'CPU Cores': os.cpus().length,
  'Total Memory': (os.totalmem() / (1024 * 1024 * 1024)).toFixed(2) + ' GB',
  'System Uptime': `${(os.uptime() / 60 / 60).toFixed(2)} hours`,
  'Current Logged User': os.userInfo().username,
  'Node Path': process.argv[0]
}

console.log(systemInfo);

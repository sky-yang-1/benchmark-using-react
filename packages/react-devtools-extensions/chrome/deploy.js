#!/usr/bin/env node


const deploy = require('../deploy');

const main = async () => await deploy('chrome');

main();

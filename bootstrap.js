#!/usr/bin/env node
const { execSync } = require('child_process');

const args = process.argv.slice(2).join(' ');
const result = execSync(`python3 -m lolcalc ${args}`, { stdio: 'inherit' });

process.exit(result?.status ?? 0);
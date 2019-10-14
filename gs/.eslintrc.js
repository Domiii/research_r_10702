module.exports = {
  'env': {
    'es6': true,
    'node': true,
  },
  'extends': [
    'google',
  ],
  'globals': {
    'Atomics': 'readonly',
    'SharedArrayBuffer': 'readonly',
  },
  'parserOptions': {
    'ecmaVersion': 2018,
    'sourceType': 'module',
  },
  'rules': {
    'require-jsdoc': 0,
    'comma-dangle': 0,
    'no-unused-vars': 0,
    'eol-last': 0,
    'valid-jsdoc': 0,
    'object-curly-spacing': 0,
    'arrow-parens': 0
  },
};

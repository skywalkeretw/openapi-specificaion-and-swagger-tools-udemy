'use strict';


/**
 * List all products
 * Returns the list of products supported by EazyShop 
 *
 * categoryId Integer  (optional)
 * returns List
 **/
exports.productsGET = function(categoryId) {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = [ {
  "quantity" : 1,
  "productId" : 0,
  "releaseDate" : "2000-01-23",
  "price" : 6.0274563,
  "name" : "name",
  "categoryName" : "categoryName"
}, {
  "quantity" : 1,
  "productId" : 0,
  "releaseDate" : "2000-01-23",
  "price" : 6.0274563,
  "name" : "name",
  "categoryName" : "categoryName"
} ];
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}


/**
 * Return product details
 * Returns the product details from  EazyShop 
 *
 * productId Integer 
 * returns Product
 **/
exports.productsProductIdGET = function(productId) {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = {
  "quantity" : 1,
  "productId" : 0,
  "releaseDate" : "2000-01-23",
  "price" : 6.0274563,
  "name" : "name",
  "categoryName" : "categoryName"
};
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}


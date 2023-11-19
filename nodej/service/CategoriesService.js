'use strict';


/**
 * Return category details
 * Returns the category details from EazyShop
 *
 * categoryId Integer 
 * returns Category
 **/
exports.categoriesCategoryIdGET = function(categoryId) {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = {
  "name" : "name",
  "categoryId" : 0
};
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}


/**
 * List all catgories
 * Returns the list of categories supported by EazyShop
 *
 * categoryId Integer  (optional)
 * returns List
 **/
exports.categoriesGET = function(categoryId) {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = [ {
  "name" : "name",
  "categoryId" : 0
}, {
  "name" : "name",
  "categoryId" : 0
} ];
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}

